import React from "react";
import { BrowserRouter as Router,  Route, Routes } from "react-router-dom";
import './App.css';
import  Login  from "./components/Pages/Login";
import  Register  from "./components/Pages/Register";
import  NavBar from "./components/NavBar";


import Gallery from "./components/Pages/Gallery";
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {


  return (
    <>
    <Router>
    <NavBar />;
    

    <div className="pages">
      <Routes>
        <Route path="/Gallery" element={<Gallery/>} />
        <Route path="/Login" element={<Login />} />
        <Route path="/Register" element={<Register />} />
        
      </Routes>
    </div>
  </Router>

  
    </>
  );
}

export default App;