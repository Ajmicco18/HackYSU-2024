import { Button, Text } from '@chakra-ui/react'
import Navbar from './Components/Navbar';
import React, { useEffect, useState } from "react"

export default function App() {

  const [data, setData] = useState(null)

  useEffect(() => {
    fetchData()
  }, []);

  async function fetchData() {
    const response = await fetch('http://127.0.0.1:8000/bets');
    const newData = await response.json();
    setData(newData)
  }

  return (
    <>
      <div>
        {
          data?.map((item) => {
            return (
              <div>
                {item.gametime}
                {item.hometeam}
                {item.awayteam}
              </div>
            )
          })
        }
        <Navbar />
        < Text fontSize='5xl' > HackYSU2024</Text>
        <Button colorScheme='blue' /*</div>onClick={queryDatabase}*/>Test</Button>
      </div>
    </>
  )
}