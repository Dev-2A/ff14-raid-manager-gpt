import React from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import JobList from "./pages/JobList";

// 예시로 홈(Home) 컴포넌트 추가
function Home() {
  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-2">FF14 레이드 매니저</h2>
      <p>환영합니다! 메뉴에서 기능을 선택하세요.</p>
    </div>
  );
}

function App() {
  return (
    <BrowserRouter>
      {/* 네비게이션바 */}
      <nav className="bg-gray-100 px-4 py-2 flex gap-4 mb-4">
        <Link to="/" className="hover:underline">홈</Link>
        <Link to="/jobs" className="hover:underline">직업 리스트</Link>
        {/* 추후 다른 메뉴 추가 */}
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/jobs" element={<JobList />} />
        {/* 추후 <Route path="/roles" element={<RoleList />} /> 등 추가 가능 */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
