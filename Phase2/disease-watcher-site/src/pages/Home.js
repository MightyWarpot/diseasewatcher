
import React from 'react'
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';

import Map from './img/map.jpg'
import Chart from './chart.js'
export default function Home() {

    const styles = useStyles()

    return (
        <div >
            <div className={styles.banner}>
                <Chart> </Chart>
                {/* <img className={styles.center} src={Map}/> */}
                {/* <div className={styles.overlay}>
                    <h2 className={styles.text}>Providing you with all the information you need</h2>
                    <Button className = {styles.buttonAbs} variant="outlined" color="Primary" href="#contained-buttons">
                          Find out more
                    </Button>
                </div> */}
            </div> 
            {/* <div className={styles.pageDisplay}>
                
            </div> */}

        </div>
    )
}


var useStyles = makeStyles({
    main: {
        background: '#212327' 
    },
    banner: {
        background: '#212327',
        color: '#aaa',
        margin: 0,
        position: 'relative'
    },
    center: {
        display: 'block',
        marginLeft: 'auto',
        marginRight: 'auto',
        width: "100%",
        opacity: 0.2
    },
    overlay: {
        position: 'absolute',
        top: '35%',
        width: '100%',
        height: '100%',
        fontSize : '1vw',
    },
    text: {
        textAlign: 'center',
        marginRight: '0%'
    },
    textInner: {
        margin: 20
    },
    buttonAbs: {
        fontSize : '1vw',
        left: '45%',
        borderColor: '#8e3fb5',
        color: '#8e3fb5',
        backgroundColor: 'rgba(142, 63, 181, 0.0)',
        padding: '0.4% 0.6%',

        "&:hover": {
            border: '1px solid #9c4fc1',
            backgroundColor: 'rgba(142, 63, 181, 0.2)'
        }
    },
    pageDisplayRow: {
        height: '50vh',
        content: '',
        display: 'table',
    },

    column: {
        float: 'left',
        width: '33.33%'
    },
    paper: {
        height: '40vh',
        width: '32vw',
        margin: '0.5vw',
        
    },
    img: {
        height: '25vh',
        textAlign: 'center',
        display: 'block',
        justifyContent: 'center',
        alignItems: 'center',
        margin: 'auto',
    },
    date: {
        position: 'absolute',
        alignItems: 'right',
        paddingLeft: '24%',
        paddingTop: '0.45%',
        fontStyle: 'italic',
    },
    dateFirst: {
        position: 'absolute',
        alignItems: 'right',
        paddingLeft: '26%',
        paddingTop: '0.45%',
        fontStyle: 'italic',
    }

    
});