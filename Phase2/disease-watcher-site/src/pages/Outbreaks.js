import React, {useState} from 'react'
import Axios from 'axios'
import TextField from '@material-ui/core/TextField';
import { makeStyles } from '@material-ui/core/styles';


export default function Outbreaks() {
    //grabbing styles
    const styles = useStyles()

    // API functions have been commented out because API proxy doesn't allow too many requests uncomment if you need to check result with backend
    // const API = Axios.create({
    //     baseURL: 'https://cors-anywhere.herokuapp.com/disease-watcher.herokuapp.com/',
    //     headers: {
    //         'content-type': 'application/json'
    //     }
    // })

    // API.get('/outbreak/?location=China&start date=11/01/1991')
    //     .then((response) => {
    //         console.log(response.data)
    //     })

    

    //functions and variables for interactions
    
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

    //Example of url that i need to request http://disease-watcher.herokuapp.com/outbreak/?location=China&disease=H7N9&start date=12/02/1998&end date=22/02/2040&region=Asia&start_index=0&end_index=10

    console.log(`http://disease-watcher.herokuapp.com/outbreak/?location=${state.location}&disease=${state.disease}&start date=${state.reportAfter}&end date=${state.reportBefore}&region=${state.region}&start_index=${state.indexStart}&end_index=${state.indexEnd}`)


    return (
        <div>
            <h2 className={styles.header}> Find Disease Information </h2>
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
                    <div>
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
    }

  }));