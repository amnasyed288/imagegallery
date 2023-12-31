import React from 'react';
import { Link, NavLink } from 'react-router-dom';

const Dashboard = ({ onLogout }) => {
  return (
    <div>
      <h1>Welcome to the Dashboard!</h1>
      <NavLink to="/Gallery">Go to Gallery</NavLink>
      <button onClick={onLogout}>Logout</button>
    </div>
  );
};

export default Dashboard;