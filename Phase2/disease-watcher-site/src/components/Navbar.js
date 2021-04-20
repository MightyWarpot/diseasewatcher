import React, {useState} from 'react'
import {Link} from 'react-router-dom'
import { makeStyles } from '@material-ui/core/styles';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'




export default function Navbar() {

    const [click, setClick] = useState(false)


    const closeMobileMenu = () => {
        setClick(false)
    }

    const styles = useStyles()

    return (
        <>
            <nav className={styles.navbar}>
                <div className = {styles.navbarContainer} >
                    <Link to='/' className={styles.navbarLogo}>
                        <h4 className={styles.heading}> Travel Guard</h4><FontAwesomeIcon icon={faUserSecret} />
                    </Link>
                    <ul className={styles.navMenu}>
                        <li className={styles.navItem}>
                            <Link to='/diseasechart' className={styles.navLinks}>
                                Disease Chart
                            </Link>
                        </li>
                        <li className={styles.navItem}>
                            <Link to='/outbreaks' className={styles.navLinks}>
                                Search
                            </Link>
                        </li>
                        
                        <li className={styles.navItem}>
                            <Link to='/advice' className={styles.navLinks}>
                                Travel Advice
                            </Link>
                        </li>
                        <li className={styles.navItem}>
                            <Link to='/Learn' className={styles.navLinks}>
                                Diseases
                            </Link>
                        </li>  
                    </ul>
                </div>
            </nav>
        </>
    );
}



var useStyles = makeStyles({
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
        transition: 'color 0.2s',

        "&:hover": {
            color: '#aef',
        }
      }
  });