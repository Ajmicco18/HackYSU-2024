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
      <Navbar />
      <div>
        {
          data?.map((item) => {
            return (
              <div>
                {item.gametime}<br />
                {item.hometeam}<br />
                {item.awayteam}<br />
              </div>
            )
          })
        }
      </div>

    </>
  )
}