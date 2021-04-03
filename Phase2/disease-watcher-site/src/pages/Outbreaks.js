import React, {useState} from 'react'
import Axios from 'axios'
import TextField from '@material-ui/core/TextField';
import { makeStyles } from '@material-ui/core/styles';
import { Button } from '@material-ui/core'

import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';


export default function Outbreaks() {
    //grabbing styles
    const styles = useStyles()

    // API functions have been commented out because API proxy doesn't allow too many requests uncomment if you need to check result with backend
    const API = Axios.create({
        baseURL: 'https://cors-anywhere.herokuapp.com/disease-watcher.herokuapp.com/',
        headers: {
            'content-type': 'application/json'
        }
    })

    const requestInfo = (request) => {
        API.get(`/outbreak/?location=${state.location}&disease=${state.disease}&start date=${state.reportAfter}&end date=${state.reportBefore}&region=${state.region}&start_index=${state.indexStart}&end_index=${state.indexEnd}`)
        .then((response) => {
            console.log(response.data)
            setTable(response.data)
        })
    } 
    
    function BasicTable() {
  
        return (
          <TableContainer component={Paper}>
            <Table className={styles.table} aria-label="simple table">
              <TableHead>
                <TableRow>
                  <TableCell>Title</TableCell>
                  <TableCell >Disease</TableCell>
                  <TableCell >Country</TableCell>
                  <TableCell >Date Reported</TableCell>
                  <TableCell >Information</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {table.map((row) => (
                  <TableRow key={table.title}>
                    <TableCell component="th" scope="row">
                      {row.title}
                    </TableCell>
                    <TableCell>{row.disease}</TableCell>
                    <TableCell>{row.location}</TableCell>
                    <TableCell>{row.date}</TableCell>
                    <TableCell>{row.body}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        );
      }
    

    // functions and variables for interactions
    
    // const [location, setLocation] = useState('');
    // const [disease, setDisease] = useState('');
    // const [continent, setContinent] = useState('');
    // const [indexStart, setIndexStart] = useState('');
    // const [indexEnd, setIndexEnd] = useState('');
    // const [reportAfter, setReportAfter] = useState('');
    // const [reportBefore, SetRepBefore] = useState('');

    const [state, setState] = useState('')
    
    const handleTextChange = e =>{
        const { target: {value, id } } = e
        setState(prev  =>({
            ...prev,
            [id] : value
        }))
    }
    console.log(state)

    const [table, setTable] = useState([])

    //Example of url that i need to request http://disease-watcher.herokuapp.com/outbreak/?location=China&disease=H7N9&start date=12/02/1998&end date=22/02/2040&region=Asia&start_index=0&end_index=10

    //console.log(`http://disease-watcher.herokuapp.com/outbreak/?location=${state.location}&disease=${state.disease}&start date=${state.reportAfter}&end date=${state.reportBefore}&region=${state.region}&start_index=${state.indexStart}&end_index=${state.indexEnd}`)


    return (
        <div>
            <h2 className={styles.header}> Find Disease Information </h2>
            <p className={styles.header}> Simply fill out the form below and we'll return any relevant information </p>
                <div className={styles.container}>
                <form className={styles.form} noValidate autoComplete="off">
                    <div>
                        <TextField id="location" label="Country" type="search" onChange={handleTextChange} />
                        <TextField id="disease" label="Type of Disease" type="search" onChange={handleTextChange} />
                        <TextField id="region" label="Continent" type="search" onChange={handleTextChange}/>
                        <TextField id="indexStart" label="Article Start Index" type="search" onChange={handleTextChange} />
                        <TextField id="indexEnd" label="Article End Index" type="search" onChange={handleTextChange} />
                        <TextField id="reportAfter" label="Outbreak Reported After" type="search" helperText="(DD/MM/YYYY)" onChange={handleTextChange} />
                        <TextField id="reportBefore" label="Oubtreak Reported Before" type="search" helperText="(DD/MM/YYYY)"  onChange={handleTextChange}/>
                    </div>
                    <div className={styles.divB}>
                        <Button variant="contained" color="primary" onClick={requestInfo}>Submit</Button>
                    </div>
                    <div>
                        {BasicTable()}
                    </div>
                </form>
            </div>
        </div>
    )
}




const useStyles = makeStyles((theme) => ({
    form: {
        '& .MuiTextField-root': {
            margin: theme.spacing(1),
            width: '25ch',
            
        },
    },
    container: {
        textAlign: 'center'
    },
    header: {
        marginLeft: '5%'
    },
    divB: {
        marginLeft: '70%',
        marginTop: '1%'
    },
    table: {
        minWidth: 650,
      },
  }));