import './App.css';
import {Typography, AppBar, Card, CardActions, Grid, CardContent, CardMedia, CssBaseline, Toolbar, Container} from '@mui/material'
import DevicesIcon from '@mui/icons-material/Devices';
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import { create } from '@mui/material/styles/createTransitions';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

function App() {

  const [device, setDevice] = useState()

  // useEffect(() => {
  //   fetch("/devicesReg").then(
  //     res => console.log(res.body)
  //   ).then(
  //     device => {
  //       setDevice(device)
  //       console.log(device);
  //     }
  //   )
  // }, [])
  const deviceInfo = async() => {
    try{
      let res = await axios.get("http://localhost:8000/devices");
      let result = res.data;
      console.log(result);
      setDevice(result);
    }catch(e){
      console.log(e);
    }
  }
  useEffect(() => {
    try{
      deviceInfo();
    }
    catch(err){
      console.log(err);
    }
    
  }, [])

 //   useEffect(() => {
//     const getDevices = async () => {
        
//         try{
//             const res = await axios.get('http://127.0.0.1:8000/devicesReg')
//             setDevice(res.data);
//             console.log(res);
//         } catch(err){
//             console.log(err);
//         }
//     }
//     getDevices()
// }, [])
  // device.map(item=>console.log(item.name))
  return (
    <>
      <CssBaseline />
      <AppBar position="relative">
        <Toolbar>
          <DevicesIcon />
          <Typography variant="h6">
            Devices Registered
          </Typography>
          </Toolbar>  
      </AppBar>
      <main>
        <div>
          <Container fixed>
            <Typography variant="h2" align="center" color="textPrimary" gutterBottom>
                Device List
              </Typography>
            <Typography variant="h5" align="center" color="textSecondary" paragraph>
                This is a device list and shows all its attributes
              </Typography>
            <div>
             <TableContainer component={Paper}>
      <Table sx={{ minWidth: 900 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>ID</TableCell>
            <TableCell align="right">Name</TableCell>
            <TableCell align="right">Commands</TableCell>
            <TableCell align="right">ConnectionInfo</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {device.map((device, id) => (
            <TableRow
              key={device.id}
              id={id}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {device.id}
              </TableCell>
              <TableCell align="right">{device.name}</TableCell>
              <TableCell align="right">{device.commands.join(",")}</TableCell>
              <TableCell align="right">{device.connectionInfo}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
            </div>
          </Container>
        </div>
      </main>
    </>
  );
}

export default App;
