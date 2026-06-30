function Sidebar() {
  return (
    <aside className="bg-white rounded-xl shadow p-5 h-full">
      <h2 className="text-lg font-semibold mb-4">
        Navigation
      </h2>

      <ul className="space-y-3">
        <li>📄 Upload Documents</li>
        <li>💬 Chat</li>
        <li>📚 Citations</li>
        <li>📊 Analytics</li>
      </ul>
    </aside>
  );
}

export default Sidebar;