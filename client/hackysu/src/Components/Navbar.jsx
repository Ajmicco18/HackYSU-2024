import React from 'react';
import { Flex, Box, Text, Button } from '@chakra-ui/react';

function Navbar() {
  return (
    <Flex
      as="nav"
      align="center"
      justify="space-between"
      padding="1rem"
      bg="blue.500"
      color="white"
    >
      <Box>
        <Text fontSize="xl" fontWeight="bold">
          Your Logo
        </Text>
      </Box>
      <Box>
        <Button variant="link" mr="4">
          Home
        </Button>
        <Button variant="link" mr="4">
          About
        </Button>
        <Button variant="link" mr="4">
          Services
        </Button>
        <Button variant="link">Contact</Button>
      </Box>
    </Flex>
  );
}

export default Navbar;