import { Button, Text } from '@chakra-ui/react'

const queryDatabase = async () => {
  //query database?
  try{
    const res = await fetch('http://127.0.0.1:8000/bets/');
    if(!res.ok){
      throw new Error('Failed to fetch data');
    }
    const data = await res.json();
    console.log(data)
  }
  catch(error){
    console.error('error fetching data: ', error);
  }
}

const App = () => {


  return(
  <div>
    <Text fontSize='5xl'>HackYSU2024</Text>
    <Button colorScheme='blue' onClick={queryDatabase}>Test</Button>
  </div>
  )
}

export default App
