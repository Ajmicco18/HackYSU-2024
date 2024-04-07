//import { useState, useEffect } from 'react';
//import { Button, Text, Card, CardHeader, CardBody, CardFooter, Box } from '@chakra-ui/react'
import { Box } from '@chakra-ui/react'
import LandingPage from '../LandingPage';
import BetsList from '../BetsList';

export default function Home() {
    return (
        <>
            <LandingPage />
            <Box maxW={'80vw'} margin={'auto'}>
                <BetsList />
            </Box>
        </>
    )

}