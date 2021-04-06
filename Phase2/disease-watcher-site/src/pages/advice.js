import React, {useState} from 'react'
import Axios from 'axios'
import TextField from '@material-ui/core/TextField';
import { makeStyles } from '@material-ui/core/styles';
import { Button } from '@material-ui/core'
import Box from '@material-ui/core/Box';
import { borders } from '@material-ui/system';
import { text } from '@fortawesome/fontawesome-svg-core';

export default function Advice() {
    //grabbing styles
    const styles = useStyles()

    // API functions have been commented out because API proxy doesn't allow too many requests uncomment if you need to check result with backend
    const [state, setState] = useState('')
    
    const handleTextChange = e =>{
        const { target: {value, id } } = e
        setState(prev  =>({
            ...prev,
            [id] : value
        }))
    }
    console.log(state)





    return (
        <div>
            <h2 className={styles.header}> Travel Advice </h2>
            <p className={styles.header}> Enter your destination country/SAR </p>
            <div className={styles.container}>
                <form className={styles.form} noValidate autoComplete="off">
                    <div>
                        <TextField id="location" label="Country/SAR" type="search" onChange={handleTextChange} />
                    
                    </div>
                    <div className={styles.divB}>
                        <Button variant="contained" color="primary" >Submit</Button>
                    </div>
                    <div className={styles.divT}>
                    <h1 >
                           Hong Kong
                        </h1>
                        <h1 className={styles.overall}>
                            Overall advice: Do not travel   
                        </h1>
                        <div > Latest update: 05 April 2021</div>
                        <div className={styles.box} >
                            <h3 className={styles.header1}> Health </h3>
                            <Box >
                                <ul>
                                    <li>
                                        COVID-19 remains a risk in Hong Kong.
                                    </li>
                                    <li>
                                    It's illegal to carry sleeping tablets and some medication without a prescription. Carry a copy of your prescription or a letter from your doctor.
                                    </li>
                                    <li>
                                    Hong Kong has very high humidity from May to October. Reduce physical and outdoor activities on very humid days.
                                    </li>
                                    <li>
                                    Hong Kong can have very high pollution levels. If you have a heart or breathing condition, do less physical activity when the air quality index health risk is high.
                                    </li>
                                    <li>
                                    Hand, foot and mouth disease (HFMD) is common. It mostly affects children aged under 10 years, but adult cases occur, particularly in young adults. Wash your hands thoroughly and often.
                                    </li>
                                    <li>
                                    Waterborne, foodborne and other infectious diseases including bird flu sometimes occur. Drink only boiled or bottled water from bottles with sealed lids. Avoid raw or undercooked food. Avoid contact with animals.
                                    </li>
                                </ul>

                            </Box>
                        </div>
                        <div className={styles.box} >
                            <h3 className={styles.header1} > Travel </h3>
                            <Box >
                                <ul>
                                    <li>
                                    You can only enter Hong Kong if you're a resident, with few exceptions. Flights to and from the United Kingdom have been suspended and travellers who have stayed for more than two hours in the United Kingdom, Ireland, Brazil or South Africa in the past 21 days, including Hong Kong residents, will be barred from arriving in Hong Kong until further notice.
                                    </li>
                                    <li>
                                    Transit services at Hong Kong International Airport are subject to a number of restrictions. Contact your airline or travel agent before travelling.
                                    </li>
                                    <li>
                                    If you have visited any country outside of mainland China, Macau and Taiwan in the 21 days prior to arrival into Hong Kong, you will be subject to 21 days compulsory quarantine in a hotel at your own expense. Your hotel reservation must be with a 'Government Designated Hotel for Quarantine'. You'll also be required to wear a wristband that monitors your location. You'll need to provide evidence of a valid room reservation before being allowed to board your flight. If you're arriving from a designated high risk country or high risk area within mainland China, you'll also need to provide a valid negative COVID-19 (nucleic acid) test issued within 72 hours before your scheduled departure flight. Check the Hong Kong Government COVID-19 website for details.
                                    </li>
                                    <li>
                                    Hong Kong has separate immigration regulations to China. You generally won't need a tourist visa if you stay less than 90 days. In all other cases, you'll need a visa. Contact the Hong Kong Economic and Trade Office in Sydney for details.
                                    </li>
                                    <li>
                                    If you're travelling from Hong Kong to China (PRC), you'll need a PRC visa. If you enter the Shenzhen Special Economic Zone, you can apply for a visa at the Shenzhen-Hong Kong border. Access to cross-border transport with mainland China may be unavailable or limited. Check arrangements with your transport provider and follow the advice of local authorities.
                                    </li>
                                    
                                </ul>

                            </Box>
                        </div>
                        
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
            width: '20%',
            marginLeft: "5%",
            display: 'flex',
            
        },
    },
    container: {
        textAlign: 'left',
        

    },
    header: {
        marginLeft: '5%'
    },
    divB: {
        marginLeft: '5%',
        marginTop: '1%'
    },
    table: {
        minWidth: 650,
      },
    divT: {
        margin: theme.spacing(13),
    },
    overall: {
        backgroundColor: "red",
        width: 500,
        textAlign: 'center',
        borderRadius: 10,
    },
    box: {
        border: 5,
        borderColor: "black",
        borderWidth: 1,
        borderStyle: "solid",
        borderRadius: 10,
        marginTop: 10,
        paddingRight: 5,
        backgroundColor: "#f4f8fc",
    },
    header1: {
        marginLeft: '3%',
        marginTop: '1%'
    }
  }));