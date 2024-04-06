const queryDatabase = async () => {
  //query database?
  try{
    const res = await fetch('/bets/');
    if(!res.ok){
      throw new Error('Failed to fetch data');
    }
    const data = await res.json();
    console.log("data: ", data);
  }
  catch(error){
    console.error('error fetching data: ', error);
  }
}

const App = () => {
  return(
  <div>
    <h1>
      test
    </h1>
    <button onClick={queryDatabase}>get something from db</button>
  </div>
  )
}

export default App
