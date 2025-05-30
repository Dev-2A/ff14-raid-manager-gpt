import React, { useState, useEffect } from 'react';
import api from '../api/axiosConfig';

function JobManager() {
  const [jobs, setJobs] = useState([]);
  const [roles, setRoles] = useState([]);
  const [newJob, setNewJob] = useState({ code: "", name: "", role_id: "" });
  const [editJob, setEditJob] = useState(null); // 수정 중인 직업

  // 직업/역할군 불러오기
  useEffect(() => {
    fetchJobs();
    api.get("roles/").then(res => setRoles(res.data));
  }, []);

  const fetchJobs = () => {
    api.get("jobs/").then(res => setJobs(res.data));
  };

  // 등록
  const handleCreate = (e) => {
    e.preventDefault();
    api.post("jobs/", {
      code: newJob.code,
      name: newJob.name,
      role_id: newJob.role_id,
      description: ""
    }).then(() => {
      setNewJob({ code: "", name: "", role_id: "" });
      fetchJobs();
    });
  };

  // 삭제
  const handleDelete = (id) => {
    if (window.confirm("정말 삭제할까요?")) {
      api.delete(`jobs/${id/}`).then(() => fetchJobs());
    }
  };

  // 수정 시작
  const startEdit
}