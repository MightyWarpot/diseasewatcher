import React, {useState} from 'react'
import {Link} from 'react-router-dom'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'




export default function Navbar() {

    const [click, setClick] = useState(false)


    const closeMobileMenu = () => {
        setClick(false)
    }

    return (
        <>
            <nav style={styles.navbar}>
                <div style = {styles.navbarContainer} >
                    <Link to='/' style={styles.navbarLogo}>
                        <h4 style={styles.heading}>DISEASE WATCHER</h4><FontAwesomeIcon icon={faUserSecret} />
                    </Link>
                    <ul style={styles.navMenu}>
                        <li style={styles.navItem}>
                            <Link to='/' style={styles.navLinks}>
                                Home
                            </Link>
                        </li>
                        <li style={styles.navItem}>
                            <Link to='/' style={styles.navLinks}>
                                Maps
                            </Link>
                        </li>
                        <li style={styles.navItem}>
                            <Link to='/' style={styles.navLinks}>
                                Vaccinations
                            </Link>
                        </li>
                        <li style={styles.navItem}>
                            <Link to='/' style={styles.navLinks}>
                                FAQ
                            </Link>
                        </li>  
                    </ul>
                </div>
            </nav>
        </>
    );
}


var styles = {
    navbar: {
        background: '#000',
        height: '100px',
        display: 'flex',
        position: 'sticky',
        borderBottom: '1px solid rgba(255, 255, 255, 0.562)',
        borderStyle: 'solid',
        justifyContent: 'center',
        alignItems: 'center',
        fontSize: '1.5vw',
        
      },
      
    navbarContainer: {
        alignItems:'center',
        height: '100px',
        display: 'flex',
        justifyContent: 'center',
      },
      
    navbarLogo: {
        fontSize: '2vw',
        display: 'flex',
        alignItems: 'center',
        color: '#fff',
        marginLeft: '20px',
        cursor: 'pointer',
        textDecoration: 'none',
        whiteSpace: 'nowrap',
      },
      
    navMenu: {
        display: 'grid',
        gridTemplateColumns: 'repeat(4, auto)',
        gridGap: '10px',
        listStyle: 'none',
        textAlign: 'center',
        width: '60vw',
        justifyContent: 'end',
        marginRight: '2rem',
        marginBottom: '2rem',
      },
      
    navLinks: {
        color: '#fff',
        display: 'flex',
        alignItems: 'center',
        textDecoration: 'none',
        padding: '0.5rem 1rem',
        height: '100%',
      }
      


  }