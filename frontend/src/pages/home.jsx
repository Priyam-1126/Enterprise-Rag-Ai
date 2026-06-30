import Navbar from "../components/layout/Navbar";
import Sidebar from "../components/layout/Sidebar";
import UploadBox from "../components/upload/UploadBox";
import ChatBox from "../components/chat/ChatBox";

function Home() {
  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />

      <div className="grid grid-cols-12 gap-6 p-6">

        <div className="col-span-3">
          <Sidebar />
        </div>

        <div className="col-span-9 space-y-6">
          <UploadBox />
          <ChatBox />
        </div>

      </div>
    </div>
  );
}

export default Home;