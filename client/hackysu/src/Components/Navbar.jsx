import React from 'react';
import { Flex, Box, Text, Button, Image } from '@chakra-ui/react';
function Navbar() {
  return (
    <Flex
      as="nav"
      align="center"
      justify="space-between"
      padding="1rem"
      bg="blue.900"
      color="gold"
    >
      <Box maxW="33px">
         <Image src="Subject.png" alt="Logo" boxSize="50px" /> 
      </Box>
      <Box>
        <Button variant="link" mr="4" color ='gold'>
          Home
        </Button>
        <Button variant="link" mr="4" color ='gold'>
          About
        </Button>
        <Button variant="link" mr="4" color ='gold'>
          Services
        </Button>
        <Button variant="link" color = 'gold'>Contact</Button>
      </Box>
    </Flex>
  );
}

export default Navbar;