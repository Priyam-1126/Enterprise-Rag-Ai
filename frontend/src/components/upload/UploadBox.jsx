import { useRef, useState } from "react";
import api from "../../api/api";

function UploadBox() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const inputRef = useRef(null);

  const selectFile = () => {
    inputRef.current.click();
  };

  async function uploadFile() {
    if (!file) {
      alert("Please select a PDF or DOCX file.");
      return;
    }

    try {
      setLoading(true);

      const formData = new FormData();
      formData.append("file", file);

      const response = await api.post("/upload/", formData);

      alert(response.data.message);

      setFile(null);
      inputRef.current.value = "";
    } catch (err) {
      console.error(err);
      alert("Upload Failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="bg-white rounded-2xl shadow-lg p-8">

      <h2 className="text-3xl font-bold mb-2">
        📄 Upload Enterprise Documents
      </h2>

      <p className="text-gray-500 mb-6">
        Upload PDF or DOCX files to build your knowledge base.
      </p>

      <div
        onClick={selectFile}
        className="border-2 border-dashed border-blue-400 rounded-xl h-48 flex flex-col justify-center items-center cursor-pointer hover:bg-blue-50 transition"
      >
        <div className="text-6xl mb-3">📁</div>

        <p className="text-lg font-semibold">
          Click here to choose a file
        </p>

        <p className="text-sm text-gray-500">
          PDF • DOCX
        </p>
      </div>

      <input
        ref={inputRef}
        hidden
        type="file"
        accept=".pdf,.docx"
        onChange={(e) => {
          if (e.target.files.length > 0) {
            setFile(e.target.files[0]);
          }
        }}
      />

      {file && (
        <div className="mt-6 bg-green-50 border border-green-300 rounded-lg p-4 flex justify-between items-center">

          <div>
            <p className="font-semibold">Selected File</p>
            <p className="text-gray-600">{file.name}</p>
          </div>

          <button
            onClick={uploadFile}
            disabled={loading}
            className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-lg"
          >
            {loading ? "Uploading..." : "Upload"}
          </button>

        </div>
      )}

    </div>
  );
}

export default UploadBox;  