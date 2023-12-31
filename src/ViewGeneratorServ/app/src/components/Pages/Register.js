import React, { useState } from "react";
import { Button, Modal } from "react-bootstrap";
import { useNavigate } from 'react-router-dom';
import "bootstrap/dist/css/bootstrap.min.css";
import axios from "axios";

const MyModal = ({ showModal, handleClose, text, btn }) => {
  return (
    <Modal show={showModal} onHide={handleClose}>
      <Modal.Header closeButton>
        <Modal.Title>Registration Status</Modal.Title>
      </Modal.Header>
      <Modal.Body>{text}</Modal.Body>
      <Modal.Footer>
        <Button variant="primary" onClick={handleClose}>
          {btn}
        </Button>
      </Modal.Footer>
    </Modal>
  );
};

const Register = () => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showModal, setShowModal] = useState(false);
  const [registrationStatus, setRegistrationStatus] = useState(null);

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validation checks
    if (!firstName || !lastName || !email || !password) {
      alert("All fields are required");
      return;
    }

    // Email validation regex
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert("Invalid email address");
      return;
    }

    // Password strength check (example: at least 8 characters)
    if (password.length < 8) {
      alert("Password must be at least 8 characters");
      return;
    }

    const formData = {
      firstName,
      lastName,
      email,
      password,
    };

    try {
      const response = await axios.post("http://event-serv/register", formData);
      console.log("Request sent ");
      
      if (response.status === 200) {
        setRegistrationStatus(response.data.registration_response.message);
        console.log(response.data)
      } 
      else {
        setRegistrationStatus(response.data.registration_response.message);
        console.error("Registration failed:", response.data);
      }
    } catch (error) {
      setRegistrationStatus("error");
      console.error("Error during registration:", error.message);
    }

    setShowModal(true);
  };

  const handleClose = () => {
    setShowModal(false);
    setEmail("");
    setLastName("");
    setPassword("");
    setFirstName("");
    setRegistrationStatus(null);
  };

  const handleBackToLogin = () => {
    setShowModal(false);
    navigate('/Login');
  };

  return (
    <>
      <section className="vh-100" style={{ backgroundColor: "#b7c0ee" }}>
        <div className="container py-5 h-100">
          <div className="row d-flex justify-content-center align-items-center h-100">
            <div className="col-12 col-md-8 col-lg-6 col-xl-5">
              <div
                className="card shadow-2-strong"
                style={{ borderRadius: "1rem" }}
              >
                <div className="card-body p-5 text-center">
                  <h2 className="fw-bold mb-5">Sign up now</h2>
                  <form onSubmit={handleSubmit}>
                    <div className="row">
                      <div className="col-md-6 mb-4">
                        <div className="form-outline mb-4">
                          <label
                            className="form-label"
                            htmlFor="form3Example1"
                            style={{ color: "#808080" }}
                          >
                            First name
                          </label>
                          <input
                            value={firstName}
                            onChange={(e) => setFirstName(e.target.value)}
                            type="text"
                            id="form3Example1"
                            className="form-control"
                          />
                        </div>
                      </div>
                      <div className="col-md-6 mb-4">
                        <div className="form-outline">
                          <label
                            className="form-label"
                            htmlFor="form3Example2"
                            style={{ color: "#808080" }}
                          >
                            Last name
                          </label>
                          <input
                            value={lastName}
                            onChange={(e) => setLastName(e.target.value)}
                            type="text"
                            id="form3Example2"
                            className="form-control"
                          />
                        </div>
                      </div>
                    </div>

                    <div className="form-outline mb-4">
                      <label
                        className="form-label"
                        htmlFor="form3Example3"
                        style={{ color: "#808080" }}
                      >
                        Email address
                      </label>
                      <input
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        type="email"
                        id="form3Example3"
                        className="form-control"
                      />
                    </div>

                    <div className="form-outline mb-4">
                      <label
                        className="form-label"
                        htmlFor="form3Example4"
                        style={{ color: "#808080" }}
                      >
                        Password
                      </label>
                      <input
                        
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        type="password"
                        id="form3Example4"
                        className="form-control"
                      />
                    </div>

                    <button
                      type="submit"
                      className="btn btn-primary btn-block mb-4"
                    >
                      Sign up
                    </button>

                    
                  </form>
                  {registrationStatus && (
                    <MyModal
                      showModal={showModal}
                      handleClose={
                        registrationStatus === "success"
                          ? handleBackToLogin
                          : handleClose
                      }
                      text={
                        registrationStatus 
                      }
                      btn={
                        registrationStatus === "success"
                          ? "Back to Login"
                          : "Ok"
                      }
                    />
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default Register;
