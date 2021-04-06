
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

            <Grid container>
                <Grid item xs={12}>
                    <h2 className={styles.text}>Current Outbreaks</h2>
                    <Grid container justify="center">
                        <Grid key={1} item>
                        <Paper elevation={0} className={styles.paper}>
                            <p className={styles.text}>Measles</p>
                            <p className={styles.textInner}>There is a current and ongoing outbreak of measles in New Zealand, with a high proportion of cases reported from the Auckland region. The New Zealand Ministry of Health is prioritising vaccination of at-risk groups including children under five years of age, people aged 15 – 29 years, Pacific peoples within those groups, children under 15 years of age who have not had a single dose of the vaccine, and babies aged 6 months and older who reside in Auckland.</p>
                        </Paper>
                        </Grid>
                        <Grid key={2} item>
                        <Paper elevation={0} className={styles.paper}>
                            <p className={styles.text}>Influenza</p>
                            <p className={styles.textInner}>In the period March 18-31, Poland’s chief veterinary office confirmed a total of 42 outbreaks of highly pathogenic avian influenza HPAI in poultry flocks. All but two of the outbreaks were in commercial flocks, and the total number of birds involved in these outbreaks were almost 1.07 million. At each location, the presence of the H5N8 virus variant was confirmed. One area has become a particular hot spot for HPAI cases, namely Kalisz County in Greater Poland (Wielkopolskie). Over this period, the first HPAI cases have been confirmed in the province of Silesia (Slaskie), and other outbreaks have hit premises in Mazovia and Lesser Poland (Malopolskie). While Silesia and Lesser Poland are neighboring provinces in the south of the country, Greater Poland and Mazovia are in central Poland.
                            These latest cases bring to 93 the number of HPAI outbreaks in the country so far this year.</p>
                        </Paper>

                        </Grid>
                        <Grid key={3} item>
                        <Paper elevation={0} className={styles.paper}>
                            <p className={styles.text}>Foot and Mouth Disease</p>
                            <p className={styles.textInner}>Families and early childhood education and care (ECEC) providers in Far North Queensland have been warned to remain on the alert for symptoms of Hand, Foot and Mouth disease (HFMD) in young children after dozens of cases were identified by public health officials in recent months.While it is common for health providers to see a small number of cases during the hotter parts of the year, this year has been especially severe.To prevent the disease spreading, ensure you practice good hand hygiene; clean and disinfect frequently touched surfaces and soiled items, including toys; avoid sharing cups, eating utensils, towels, and clothing; and teach children about cough and sneeze etiquette. </p>
                        </Paper>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>



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
        height: '30vh',
        width: '32vw',
    },
    
});