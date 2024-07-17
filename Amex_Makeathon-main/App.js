import './App.css';
import React, { useState } from 'react';
import { useAuth0 } from '@auth0/auth0-react';

const LoginButton = () => {
  const { loginWithRedirect } = useAuth0();

  const handleLogin = async () => {
    try {
      await loginWithRedirect({
        screen_hint: 'biometric',
      });
    } catch (error) {
      console.error('Biometric authentication failed:', error);
    }
  };

  return (
    <button onClick={handleLogin}>
      Login with Biometric
    </button>
  );
};

const App = () => {
  return (
    <div>
      <h1>Biometric Authentication Demo</h1>
      <LoginButton />
    </div>
  );
};

export default App;




// changes in index.js

// import React from 'react';
// import ReactDOM from 'react-dom/client';
// import './index.css';
// import App from './App';
// import reportWebVitals from './reportWebVitals';
// import { Auth0Provider } from '@auth0/auth0-react';

// ReactDOM.render(
//   <Auth0Provider
//     domain=""
//     clientId=""
//     redirectUri={window.location.origin}
//   >
//     <App />
//   </Auth0Provider>,
//   document.getElementById('root')
// );

// reportWebVitals();


