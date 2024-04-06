import { useState, useEffect } from 'react';
import { Button, Text, Card, CardHeader, CardBody, CardFooter, Box } from '@chakra-ui/react'
import Navbar from './Components/Navbar';
import LandingPage from './Components/LandingPage';
import Footer from './Components/Footer';
import BetsList from './pages/BetsList';

const App = () => {



  return(
  <div>
    <Navbar />
    <LandingPage />
     <BetsList />
    <Footer />
  </div>
  )
}

export default App
