
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

            <Grid container>
                <Grid item xs={12}>
                    <h1 className={styles.text}>Current Outbreaks</h1>
                    <Grid container justify="center">
                        <Grid key={1} item>
                        <Paper elevation={3} className={styles.paper}>
                            <span className={styles.dateFirst}>March 2, 2021</span>
                            <h2 className={styles.text}>Norovirus </h2>
                            <p className={styles.textInner}>The Taiwan CDC is reporting the number of visits to hospitals for diarrhea has recently increased, and the pathogens detected in cluster incidents are mainly norovirus, and most of them occur in the catering and hotel industry.</p>
                            <img
                                className={styles.img}
                                src="http://outbreaknewstoday.com/wp-content/uploads/2019/01/21348_lores.jpg"
                                alt="new"
                                />
                        </Paper>
                        </Grid>
                        <Grid key={2} item>
                        <Paper elevation={1} className={styles.paper}>
                            <span className={styles.date}>November 21, 2020</span>
                            <h2 className={styles.text}>Influenza</h2>
                            <p className={styles.textInner}>Federal and state authorities say a case of low pathogenic avian influenza has been detected in a commercial poultry flock in western Kentucky.</p>
                            <img
                                className={styles.img}
                                src="http://outbreaknewstoday.com/wp-content/uploads/2017/03/urica-1251980_640.jpg"
                                alt="new"
                                />
                        </Paper>

                        </Grid>
                        <Grid key={3} item>
                        <Paper elevation={1} className={styles.paper}>
                            <span className={styles.date}>December 15, 2020</span>
                            <h2 className={styles.text}>Polio</h2>
                            <p className={styles.textInner}>Polio outbreaks have been reported in the following Asian countries: Afghanistan, Burma (Myanmar), China, Malaysia, Pakistan, The Philippines, Tajikistan and Yemen. </p>
                            <img
                                className={styles.img}
                                src="http://outbreaknewstoday.com/wp-content/uploads/2021/02/Capture-2.png"
                                alt="new"
                                />
                        </Paper>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>

            <br/>

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