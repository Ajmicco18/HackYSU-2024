import { useState, useEffect } from 'react';
import { Button, Text, Card, CardHeader, CardBody, CardFooter, Box } from '@chakra-ui/react'
import Navbar from './Components/Navbar';
import BetsList from './pages/BetsList';




const App = () => {


  return(
  <div>
    <Navbar />
    <BetsList/>
  </div>
  )
}

export default App
