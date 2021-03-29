import React from 'react'
import Axios from 'axios'
import TextField from '@material-ui/core/TextField';
import { makeStyles } from '@material-ui/core/styles';

export default function Outbreaks() {

    const API = Axios.create({
        baseURL: 'https://cors-anywhere.herokuapp.com/disease-watcher.herokuapp.com/',
        headers: {
            'content-type': 'application/json'
        }
    })

    API.get('/outbreak/?location=China&start date=11/01/1991')
        .then((response) => {
            console.log(response.data)
        })

    const styles = useStyles()


    return (
        <div>
            <h2 className> Find Disease Information </h2>
                <div className={styles.container}>
                <form className={styles.form} noValidate autoComplete="off">
                    <div>
                        <TextField id="location" label="Location" type="search" />
                        <TextField id="disease" label="Type of Disease" type="search" />
                        <TextField id="reportAfter" label="Outbreak Reported After (DD/MM/YYYY)" type="search" />
                        <TextField id="reportBefore" label="Oubtreak Reported Before (DD/MM/YYYY)" type="search" />
                        <TextField id="continent" label="Continent" type="search" />
                        <TextField id="indexStart" label="Article Start Index" type="search" />
                        <TextField id="indexEnd" label="Article End Index" type="search" />
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
    }

  }));