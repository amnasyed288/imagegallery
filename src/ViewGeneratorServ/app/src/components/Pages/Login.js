import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import axios from "axios";
import { NavLink } from "react-router-dom";
import Gallery from "./Gallery";

const Login = ({ isLoggedIn, setIsLoggedIn }) => {

  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");
  const [userId, setUserId] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = {
      email: email,
      password: pass,
    };

    try {
      // Assuming your login microservice is running at http://user-serv:5001
      const response = await axios.post(
        "http://event-serv/login",
        formData
      );
      console.log(response.status);
      console.log("Login Request sent ");

      if (response.status === 200) {
        // Login successful
        console.log("Login successful:", response.data.login_responses);
        console.log("BEFORE: " + isLoggedIn);
        setIsLoggedIn(true);
        setUserId(response.user_id);
        console.log("USERID: " + userId)
        console.log("After: " + isLoggedIn);
        // console.log(isLoggedIn);
      } else {
        // Handle login failure
        console.error("Login failed:", response.data);
      }
    } catch (error) {
      // Handle error (e.g., network issue)
      console.error("Error during login:", error.message);
    }
  };

  return (
    <>
      {isLoggedIn ?
        <Gallery userId={userId} />
        :
        <section className="vh-100" style={{ height: "100vh", backgroundColor: "#b7c0ee" }}>
          <div className="container py-5 h-100">
            <div className="row d-flex justify-content-center align-items-center h-100">
              <div className="col-12 col-md-8 col-lg-6 col-xl-5">
                <div
                  className="card shadow-2-strong"
                  style={{ borderRadius: "1rem" }}
                >
                  <div className="card-body p-5 text-center">
                    <h3 className="mb-5">Sign in</h3>

                    <div className="form-outline mb-4">
                      <label
                        className="form-label"
                        htmlFor="typeEmailX-2"
                        style={{ color: "#808080" }}
                      >
                        Email
                      </label>
                      <input
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        type="email"
                        id="typeEmailX-2"
                        className="form-control form-control-lg"
                      />
                    </div>

                    <div className="form-outline mb-4">
                      <label
                        className="form-label"
                        htmlFor="typePasswordX-2"
                        style={{ color: "#808080" }}
                      >
                        Password
                      </label>
                      <input
                        value={pass}
                        onChange={(e) => setPass(e.target.value)}
                        type="password"
                        id="typePasswordX-2"
                        className="form-control form-control-lg"
                      />
                    </div>



                    <button
                      className="btn btn-primary btn-lg btn-block"
                      onClick={handleSubmit}
                      type="submit"
                    >
                      Login
                    </button>

                    <div>
                      <p className="mb-4 ">
                        Don't have an account?{" "}
                        <NavLink
                          exact='true'
                          to="/Register"
                        >
                          SignUp
                        </NavLink>
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      }
    </>
  );
};

export default Login;
