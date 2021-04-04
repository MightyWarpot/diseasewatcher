
import React from 'react'
import { makeStyles } from '@material-ui/core/styles';

import Map from './img/map.jpg'
import Chart from './chart.js'
export default function Home() {

    const styles = useStyles()

    return (
        <div>
            
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
    pageDisplay: {
        backgroundColor: '#0e3c5d',
        margin: '0',
        height: '200px'
        
    }
    
});