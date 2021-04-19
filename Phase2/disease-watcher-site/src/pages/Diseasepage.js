import { Button } from '@material-ui/core'
import React, {useEffect, useState} from 'react'
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Map from './img/map.jpg'
import Notcovidchart from './notcovidchart.js'
import Axios from 'axios'
import Box from '@material-ui/core/Box';
export default function Diseasepage() {

    const styles = useStyles()
    const [country, setCountry] = useState('')
    const [disease, setDisease] = useState()
    const [date, setDate] = useState()
    const [traveldata, setTravel] = useState()
    const API = Axios.create({
      baseURL: 'https://cors-anywhere.herokuapp.com/disease-watcher.herokuapp.com/',
      headers: {
          'content-type': 'application/json'
      }
    })
    const TravelAPI = Axios.create({
      baseURL: 'https://api.tugo.com/v1/travelsafe/countries/',
      headers: {
          'content-type': 'application/json',
          'X-Auth-API-Key': '2ndchevugmej6p4whk6zjebg'

      }
    })
    let convertedtime
    if (date) {
      convertedtime = new Date(date)
      let dd = convertedtime.getDate()
      let month = convertedtime.getMonth() + 1
      if(dd<10) {
          dd='0'+dd;
      }
      if(month<10) {
        month='0'+month;
      } 
      convertedtime = dd + "/" + month + "/"  + convertedtime.getFullYear()
    }
    
    const requestInfo = () => {
        
      var location = (typeof country === 'undefined') ? " ": country
      var disease = (typeof disease === 'undefined') ? " ": disease
      var reportAfter = (typeof convertedtime === 'undefined') ? " " : convertedtime
      console.log("searching")

      API.get(`/outbreak/?location=${location}&disease=${disease}&start date=${reportAfter}`)
      .then((response) => {
          console.log(response)
          // setTable(response.data)
      })
    } 
    const travelData = (country) => {
      let countryID = countryIds[country] 
      console.log(countryID)
      TravelAPI.get(`${countryID}`)
      .then((res) => {
        console.log(res.data)
        setTravel(res.data)
      })
    }
    useEffect(() => {
      if (country && disease && date) {
        requestInfo()
        travelData(country)
      }
    }, [country])
    
    return (
        <div>
            
            <div className={styles.banner}>
                <Notcovidchart setCountry={setCountry} setDisease={setDisease} setDate={setDate}> </Notcovidchart>
                {/* <img className={styles.center} src={Map}/> */}
                {/* <div className={styles.overlay}>
                    <h2 className={styles.text}>Providing you with all the information you need</h2>
                    <Button className = {styles.buttonAbs} variant="outlined" color="Primary" href="#contained-buttons">
                          Find out more
                    </Button>
                </div> */}
                <div className={styles.content}>
                  <Typography variant="h6" noWrap>
                    Disease Report
                  </Typography>
                  <Typography paragraph>
                    {country} {disease} {date}
                  </Typography>
                  <Typography variant="h6" noWrap>
                    Travel Advice
                  </Typography>
                  <Typography paragraph>
                  {traveldata && <Typography > {traveldata.advisories.description}</Typography>}
                    {traveldata && <Typography className={styles.advice}> {traveldata.advisoryText}</Typography>}
                  </Typography>
                  <div className={styles.box} >
                    <h3 className={styles.header1}> Health Advisories </h3>
                    <Box >
                      
                        {traveldata && traveldata.health.diseasesAndVaccinesInfo
                          && <ul>{traveldata.health.diseasesAndVaccinesInfo['Food/Water'].map(region => {
                          return (<li> {region.category} </li>)
                }) }</ul>}
                      
                      
                    </Box>
                    </div>
                </div>
            </div>
            {/* <div className={styles.pageDisplay}>
                
            </div> */}
        </div>
    )
}


var useStyles = makeStyles({
    banner: {
        background: '#212327',
        color: '#dddfe8',
        margin: 0,
        position: 'relative',
        display: 'flex',
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
        
    },
    content: {
      width: "30%",
      flexGrow: 1,
      padding: "5px",
    },
    advice: {
      backgroundColor: "red",
      width: "70%",
      textAlign: 'center',
      borderRadius: 10,
      color: "black",
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
      color: "black",
      paddingLeft: 10,
    },
    header1: {
      color: "black",
    }
    
});

const countryIds = {"Afghanistan": "AF", "Aland Islands": "AX", "Albania": "AL", "Algeria": "DZ", "American Samoa": "AS", "Andorra": "AD", "Angola": "AO", "Anguilla": "AI", "Antarctica": "AQ", "Antigua And Barbuda": "AG", "Argentina": "AR", "Armenia": "AM", "Aruba": "AW", "Australia": "AU", "Austria": "AT", "Azerbaijan": "AZ", "Bahamas": "BS", "Bahrain": "BH", "Bangladesh": "BD", "Barbados": "BB", "Belarus": "BY", "Belgium": "BE", "Belize": "BZ", "Benin": "BJ", "Bermuda": "BM", "Bhutan": "BT", "Bolivia": "BO", "Bosnia And Herzegovina": "BA", "Botswana": "BW", "Bouvet Island": "BV", "Brazil": "BR", "British Indian Ocean Territory": "IO", "Brunei Darussalam": "BN", "Bulgaria": "BG", "Burkina Faso": "BF", "Burundi": "BI", "Cambodia": "KH", "Cameroon": "CM", "Canada": "CA", "Cape Verde": "CV", "Cayman Islands": "KY", "Central African Republic": "CF", "Chad": "TD", "Chile": "CL", "China": "CN", "Christmas Island": "CX", "Cocos (Keeling) Islands": "CC", "Colombia": "CO", "Comoros": "KM", "Congo": "CG", "Congo, Democratic Republic": "CD", "Cook Islands": "CK", "Costa Rica": "CR", "Cote D'Ivoire": "CI", "Croatia": "HR", "Cuba": "CU", "Cyprus": "CY", "Czech Republic": "CZ", "Denmark": "DK", "Djibouti": "DJ", "Dominica": "DM", "Dominican Republic": "DO", "Ecuador": "EC", "Egypt": "EG", "El Salvador": "SV", "Equatorial Guinea": "GQ", "Eritrea": "ER", "Estonia": "EE", "Ethiopia": "ET", "Falkland Islands (Malvinas)": "FK", "Faroe Islands": "FO", "Fiji": "FJ", "Finland": "FI", "France": "FR", "French Guiana": "GF", "French Polynesia": "PF", "French Southern Territories": "TF", "Gabon": "GA", "Gambia": "GM", "Georgia": "GE", "Germany": "DE", "Ghana": "GH", "Gibraltar": "GI", "Greece": "GR", "Greenland": "GL", "Grenada": "GD", "Guadeloupe": "GP", "Guam": "GU", "Guatemala": "GT", "Guernsey": "GG", "Guinea": "GN", "Guinea-Bissau": "GW", "Guyana": "GY", "Haiti": "HT", "Heard Island & Mcdonald Islands": "HM", "Holy See (Vatican City State)": "VA", "Honduras": "HN", "Hong Kong": "HK", "Hungary": "HU", "Iceland": "IS", "India": "IN", "Indonesia": "ID", "Iran, Islamic Republic Of": "IR", "Iraq": "IQ", "Ireland": "IE", "Isle Of Man": "IM", "Israel": "IL", "Italy": "IT", "Jamaica": "JM", "Japan": "JP", "Jersey": "JE", "Jordan": "JO", "Kazakhstan": "KZ", "Kenya": "KE", "Kiribati": "KI", "Korea": "KR", "Kuwait": "KW", "Kyrgyzstan": "KG", "Lao People's Democratic Republic": "LA", "Latvia": "LV", "Lebanon": "LB", "Lesotho": "LS", "Liberia": "LR", "Libyan Arab Jamahiriya": "LY", "Liechtenstein": "LI", "Lithuania": "LT", "Luxembourg": "LU", "Macao": "MO", "Macedonia": "MK", "Madagascar": "MG", "Malawi": "MW", "Malaysia": "MY", "Maldives": "MV", "Mali": "ML", "Malta": "MT", "Marshall Islands": "MH", "Martinique": "MQ", "Mauritania": "MR", "Mauritius": "MU", "Mayotte": "YT", "Mexico": "MX", "Micronesia, Federated States Of": "FM", "Moldova": "MD", "Monaco": "MC", "Mongolia": "MN", "Montenegro": "ME", "Montserrat": "MS", "Morocco": "MA", "Mozambique": "MZ", "Myanmar": "MM", "Namibia": "NA", "Nauru": "NR", "Nepal": "NP", "Netherlands": "NL", "Netherlands Antilles": "AN", "New Caledonia": "NC", "New Zealand": "NZ", "Nicaragua": "NI", "Niger": "NE", "Nigeria": "NG", "Niue": "NU", "Norfolk Island": "NF", "Northern Mariana Islands": "MP", "Norway": "NO", "Oman": "OM", "Pakistan": "PK", "Palau": "PW", "Palestinian Territory, Occupied": "PS", "Panama": "PA", "Papua New Guinea": "PG", "Paraguay": "PY", "Peru": "PE", "Philippines": "PH", "Pitcairn": "PN", "Poland": "PL", "Portugal": "PT", "Puerto Rico": "PR", "Qatar": "QA", "Reunion": "RE", "Romania": "RO", "Russian Federation": "RU", "Rwanda": "RW", "Saint Barthelemy": "BL", "Saint Helena": "SH", "Saint Kitts And Nevis": "KN", "Saint Lucia": "LC", "Saint Martin": "MF", "Saint Pierre And Miquelon": "PM", "Saint Vincent And Grenadines": "VC", "Samoa": "WS", "San Marino": "SM", "Sao Tome And Principe": "ST", "Saudi Arabia": "SA", "Senegal": "SN", "Serbia": "RS", "Seychelles": "SC", "Sierra Leone": "SL", "Singapore": "SG", "Slovakia": "SK", "Slovenia": "SI", "Solomon Islands": "SB", "Somalia": "SO", "South Africa": "ZA", "South Georgia And Sandwich Isl.": "GS", "Spain": "ES", "Sri Lanka": "LK", "Sudan": "SD", "Suriname": "SR", "Svalbard And Jan Mayen": "SJ", "Swaziland": "SZ", "Sweden": "SE", "Switzerland": "CH", "Syrian Arab Republic": "SY", "Taiwan": "TW", "Tajikistan": "TJ", "Tanzania": "TZ", "Thailand": "TH", "Timor-Leste": "TL", "Togo": "TG", "Tokelau": "TK", "Tonga": "TO", "Trinidad And Tobago": "TT", "Tunisia": "TN", "Turkey": "TR", "Turkmenistan": "TM", "Turks And Caicos Islands": "TC", "Tuvalu": "TV", "Uganda": "UG", "Ukraine": "UA", "United Arab Emirates": "AE", "United Kingdom": "GB", "United States": "US", "United States Outlying Islands": "UM", "Uruguay": "UY", "Uzbekistan": "UZ", "Vanuatu": "VU", "Venezuela": "VE", "Viet Nam": "VN", "Virgin Islands, British": "VG", "Virgin Islands, U.S.": "VI", "Wallis And Futuna": "WF", "Western Sahara": "EH", "Yemen": "YE", "Zambia": "ZM", "Zimbabwe": "ZW"}