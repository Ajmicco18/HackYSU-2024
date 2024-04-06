//import { useState, useEffect } from 'react';
//import { Button, Text, Card, CardHeader, CardBody, CardFooter, Box } from '@chakra-ui/react'
import { Box } from '@chakra-ui/react'
import BetCard from './Components/BetCard';
import Navbar from './Components/Navbar';
import LandingPage from './Components/LandingPage';
import Footer from './Components/Footer';
import BetsList from './Components/BetsList';

const App = () => {



  return(
  <div>
    <Navbar />
    <LandingPage />
      <Box maxW={'80vw'} margin={'auto'}>
        <BetsList />
      </Box>
    <Footer />
  </div>
  )
}

export default App
