import Dialog from '@material-ui/core/Dialog';
import PropTypes from 'prop-types'
import React from 'react'
import Button from '@material-ui/core/Button'
import { makeStyles } from '@material-ui/core/styles';

const Modal = ({ open, handleClose, info }) => {
  const styles = useStyles()
  return (
    <Dialog onClose={handleClose} open={open}>
      <h1  className={styles.dialog} > {info && info.category}</h1>
      <p  className={styles.dialog} >  {info && info.description} </p>
    </Dialog>
  )
}
var useStyles = makeStyles({
  dialog: {
    paddingLeft: 10,
    paddingRight: 10,
  }
})
Modal.propTypes = {
  open: PropTypes.bool,
  handleClose: PropTypes.func,
  info: PropTypes.object,
}

export default Modal
