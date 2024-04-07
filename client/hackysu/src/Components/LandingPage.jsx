//import React from 'react';
import { Flex, Box, Heading, Text, Button } from '@chakra-ui/react';

const scrollToElement = () => {
  document.getElementById('firstBetCard').scrollIntoView({
    behavior: 'smooth'
  });

}


const LandingPage = () => {
  return (
    <Box>
      <Flex
        height="100vh"
        justify="center"
        align="center"
        direction="column"
        bg="#7B0323"
        color="white"
      >
        <Box textAlign="center">
          <Heading as="h1" size="2xl" mb="4" color="gold">
            Welcome to LeGamble!
          </Heading>
          <Text fontSize="xl" mb="8" color="gold">
            Discover the amazing features we offer!
          </Text>
          <Button onClick={scrollToElement} backgroundColor="blue.900" color="white" mr="4">
            View Bets
          </Button>
          <a href="\AboutPage">
            <Button backgroundColor="blue.900" color="white" mr="4">
              Learn More
            </Button>
          </a>

        </Box>
      </Flex>
      <div id='firstBetCard' style={{ maxWidth: '100vw', paddingTop: '100px', backgroundColor: '#7B0323' }}></div>
    </Box>

  );
};

export default LandingPage;