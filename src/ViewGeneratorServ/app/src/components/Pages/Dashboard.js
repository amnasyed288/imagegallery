import React from 'react';
import { Link } from 'react-router-dom';

const Dashboard = ({ onLogout }) => {
 return (
    <div>
      <h1>Welcome to the Dashboard!</h1>
      <Link to="/Gallery">Go to Gallery</Link>
      <button onClick={onLogout}>Logout</button>
    </div>
 );
};

export default Dashboard;