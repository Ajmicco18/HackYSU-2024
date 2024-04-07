import { useState, useEffect } from 'react';
//import { Text } from '@chakra-ui/react';
import BetCard from './BetCard';
const BetsList = () => {
    const [bets, setBets] = useState();~

    
    
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
       
        
       
        <div>
        {bets.map((bet, index) => {
          if (index === 0){
           return (
             <div key={`${bet._id}-${index}`}>
            <BetCard GameDay = {bet.GameDay} GameTime = {bet.GameTime} HomeTeam = {bet.HomeTeam} MoneyLine1 = {bet.MoneyLine1} VisitorTeam = {bet.VisitorTeam} Website = {bet.Website}/>
              </div>
           ) 
          }
          return(
            <div key={`${bet._id}-${index}`}>
              <BetCard GameDay = {bet.GameDay} GameTime = {bet.GameTime} HomeTeam = {bet.HomeTeam} MoneyLine1 = {bet.MoneyLine1} VisitorTeam = {bet.VisitorTeam} Website = {bet.Website}/>
          </div>
          )
        })}
        </div>
    
    )
  }
  }

export default BetsList;