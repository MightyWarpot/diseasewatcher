import { Button } from '@material-ui/core'
import React from 'react'

import Map from './img/map.jpg'

export default function Home() {
    return (
        <div>
            <div style={styles.banner}>
                <img style={styles.center} src={Map}/>
                <div style={styles.overlay}>
                    <h2 style={styles.text}>Providing you with all the information you need</h2>
                    <Button style = {styles.buttonAbs} variant="outlined" color="Primary" href="#contained-buttons">
                          Find out more
                    </Button>
                </div>
            </div> 
            <div style={styles.pageDisplay}>
                
            </div>
        </div>
    )
}


const styles = {
    banner: {
        background: '#000',
        color: '#fff',
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
        backgroundColor: 'rgba(142, 63, 181, 0.1)',
        padding: '0.4% 0.6%'
    },
    pageDisplay: {
        backgroundColor: '#0e3c5d',
        margin: '0',
        height: '200px'
        
    }
    
}