import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate
} from 'react-router-dom';
import "./App.css"
import Home from './Components/Pages/Home';
import AboutPage from './Components/Pages/AboutPage';
import Navbar from './Components/Navbar';
import ServicesPage from './Components/Pages/ServicesPage';
import Contacts from './Components/Pages/Contacts';


function App() {

  return (
    <>
      <Navbar />
      <Router>
        <Routes>
          <Route
            exact
            path="/"
            element={<Home />} />
          <Route
            exact
            path="/AboutPage"
            element={<AboutPage />} />
          <Route
            exact
            path="/Services"
            element={<ServicesPage />} />
          <Route
            exact
            path="/Contact"
            element={<Contacts />} />
        </Routes>
      </Router>
      <footer>
        &copy; {new Date().getFullYear()} LeGamble. All rights reserved.
      </footer >
    </>
  )
}

export default App
