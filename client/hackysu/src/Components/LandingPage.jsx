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
      <Box margin={'auto'}>
      <Heading as="h1" size="2xl" mb="4" color ="gold">
        Welcome to Our Website
      </Heading>
      <Text fontSize="xl" mb="8" color = "blue.400">
        Discover the amazing features we offer!
      </Text>
      <Box>
        <Button  onClick={scrollToElement} colorScheme="blue" mr="4">
          Get Started
        </Button>
        <Button variant="outline" colorScheme="whiteAlpha">
          Learn More
        </Button>
      </Box>
      </Box>
    </Flex>
    <div id = 'firstBetCard' style = {{ maxWidth: '100vw', paddingTop : '100px', backgroundColor: '#7B0323'}}></div>
    </Box>
  );
};

export default LandingPage;