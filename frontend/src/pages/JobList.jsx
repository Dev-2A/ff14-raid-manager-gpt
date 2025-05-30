import React, { useEffect, useState } from 'react';
import axios from 'axios';

function JobList() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/jobs/')
      .then(res => setJobs(res.data))
      .catch(err => console.error('직업 불러오기 오류:', err));
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-2">직업 리스트</h2>
      <ul>
        {jobs.map(job => (
          <li key={job.id}>
            <strong>{job.name}</strong> ({job.code}) / 역할군: {job.role?.name}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default JobList;