import { useState, useEffect } from 'react';
import { Button, Text, Card, CardHeader, CardBody, CardFooter, Box } from '@chakra-ui/react'

const BetsList = () => {
    const [bets, setBets] = useState();

    
    
    useEffect(() => {
  
      async function query() {
  
        try{
          const res = await fetch('http://127.0.0.1:8000/bets/');
          if(!res.ok){
            throw new Error('Failed to fetch data');
          }
          const data = await res.json();
          setBets(data)
        }
        catch(error){
          console.error('error fetching data: ', error);
        }
      }
  
      query();
  
    }, [])
  
    
    if (bets) {
      console.log(bets)
    return(
       
        
       
        <div >
        {bets.map(({_id, awayteam, hometeam, gametime}, index) => (
          <div key={`${_id}-${index}`}>
            <p size="3xl">Game Time: {gametime}</p>
            <p size="3xl">Home Team: {hometeam}</p>
            <p size="3xl">Away Team: {awayteam}</p>
        </div>
    ))}
      </div>
    
    )
  }
  }

export default BetsList;