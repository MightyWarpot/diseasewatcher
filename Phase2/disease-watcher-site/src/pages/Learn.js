
import React, { useRef, useState, Suspense } from 'react'
import { Canvas, useFrame } from '@react-three/fiber'
import { makeStyles } from '@material-ui/core/styles';

import Paper from '@material-ui/core/Paper';

import { useGLTF, OrbitControls } from '@react-three/drei'

import Grid from '@material-ui/core/Grid';
  
  export default function Learn() {

    const styles = useStyles()

    return (
      <div >


      <Grid container  style={{ height: 600}}>
        
        <Grid item xs={4}>
          <div style = {{ height: '50vh'}}>
          <Canvas style = {{background: '#000d'}}>
            <ambientLight intensity={0.3} />
            <Suspense fallback={null}>
            <spotLight position={[10, 10, 10]} angle={0.15} penumbra={1}  />
            <pointLight position={[-10, -10, -10]}  />
              <Fungi/>
            </Suspense>
            <OrbitControls/>
          </Canvas>
          </div>
          <Paper elevation={1} className={styles.paper}>
            <h2 className={styles.text}>Fungal Infections</h2>
            <p className={styles.textInner}>Fungal infections can affect anyone, and they can appear on several parts of the body. A jock with athlete’s foot, a baby with thrush, and a woman with a vaginal yeast infection are just a few examples.
              <br/>
              <br/>
              Fungi are microorganisms characterized by a substance in their cell walls called chitin. Some fungi, like many types of mushrooms, are edible. Other types of fungi, like aspergillus, can be extremely dangerous and lead to life-threatening diseases.
              <br/>
              <br/>
              Different types of fungi can cause fungal infections. In some cases, fungi that aren’t typically found on or inside your body can colonize it and cause an infection. In other cases, fungi that are normally present on or inside your body can multiply out of control and cause an infection.
              <br/>
              <br/>
              Fungal infections can be contagious. They can spread from one person to another. In some cases, you can also catch disease-causing fungi from infected animals or contaminated soil or surfaces.</p>
          </Paper>
          
        </Grid>
        <Grid item xs={4}>
        <div style = {{ height: '50vh'}}>
          <Canvas style = {{background: '#000d'}}>
            <ambientLight intensity={0.5} />
            <Suspense fallback={null}>
              <Bacteria/>
            </Suspense>
            <OrbitControls/>
          </Canvas>
        </div>
        <Paper elevation={1} className={styles.paper}>
            <h2 className={styles.text}>Bacterial Infections</h2>
            <p className={styles.textInner}>A bacterial infection occurs when bacteria enter your body and begin to multiply.
              <br/>
              <br/>
              Not all bacteria are bad. In fact, various species of bacteria begin to colonize our bodies shortly after we’re born. These bacteria are harmless and can offer us benefits sometimes, like helping with digestion.
              <br/>
              <br/>
              Some types of bacteria, referred to as pathogenic bacteria, are harmful to us. When they infect us, they can cause disease.
              <br/>
              <br/>
              Some of these infections can become serious, so be sure to see your doctor if you think you have a bacterial infection. For example, a minor skin infection may develop into cellulitis if left untreated.
              <br/>
              <br/>
              Additionally, some infections can lead to a life-threatening condition called sepsis. It’s an extreme response by your body to an infection.
            </p>
          </Paper>
        </Grid>
        <Grid item xs={4}>
          <div style = {{ height: '50vh'}}>
            <Canvas style = {{background: '#000d'}}>
              <ambientLight intensity={0.4} />
              <Suspense fallback={null}>
                <Virus/>
              </Suspense>
              <OrbitControls/>
            </Canvas>
          </div>
          <Paper elevation={1} className={styles.paper}>
            <h2 className={styles.text}>Viral Infections</h2>
            <p className={styles.textInner}>Viruses are very tiny germs. They are made of genetic material inside of a protein coating. Viruses cause familiar infectious diseases such as the common cold, flu and warts. They also cause severe illnesses such as HIV/AIDS, Ebola, and COVID-19.
              <br/>
              <br/>
              Viruses are like hijackers. They invade living, normal cells and use those cells to multiply and produce other viruses like themselves. This can kill, damage, or change the cells and make you sick. Different viruses attack certain cells in your body such as your liver, respiratory system, or blood.
              <br/>
              <br/>
              When you get a virus, you may not always get sick from it. Your immune system may be able to fight it off.
              <br/>
              <br/>
              For most viral infections, treatments can only help with symptoms while you wait for your immune system to fight off the virus. Antibiotics do not work for viral infections. There are antiviral medicines to treat some viral infections. Vaccines can help prevent you from getting many viral diseases.
            </p>
          </Paper>
        </Grid>
      </Grid>
      </div>
    )
  }

  function Fungi(props) {
    const group = useRef()
    const { nodes, materials } = useGLTF('renders/Spore.glb')
    return (
      <group ref={group} {...props} dispose={null}>
        <group rotation={[-Math.PI / 2, 0, 0]}  scale={[0.02, 0.02, 0.02]}>
          <mesh geometry={nodes.Mesh_0002.geometry} material={materials.material}> <meshStandardMaterial color={'a9a9a9'} /> </mesh>
          <mesh geometry={nodes.Mesh_1002.geometry} material={materials['default']}><meshStandardMaterial color={'a9a9a9'} /></mesh>
        </group>
      </group>
    )
  }


  function Bacteria(props) {
    const group = useRef()
    const { nodes, materials } = useGLTF('renders/Bacteria.glb')
    return (
      <group ref={group} {...props} dispose={null}>
        <group position={[-1, 0, -5]} rotation={[-Math.PI / 2, 0, 0]} scale={[0.08, 0.08, 0.081]}>
          <group position={[0, -30, -20]} rotation={[-1.56, 0, 0]}>
            <mesh geometry={nodes.Mesh_0001.geometry} material={materials.color_11593967} />
            <mesh geometry={nodes.Mesh_1001.geometry} material={materials.color_14860437} />
            <mesh geometry={nodes.Mesh_2001.geometry} material={materials.color_16711762} />
            <mesh geometry={nodes.Mesh_3001.geometry} material={materials.color_16776704} />
            <mesh geometry={nodes.Mesh_4001.geometry} material={materials.color_16777215} />
            <mesh geometry={nodes.Mesh_5001.geometry} material={materials.color_40919} />
            <mesh geometry={nodes.Mesh_6001.geometry} material={materials.color_4390986} />
            <mesh geometry={nodes.Mesh_7001.geometry} material={materials.color_6306067} />
          </group>
        </group>
      </group>
    )
  }

  function Virus(props) {
    const group = useRef()
    const { nodes, materials } = useGLTF('renders/corona.glb')
    return (
      <group ref={group} {...props} dispose={null} scale={[0.07, 0.07, 0.07]} >
        <mesh geometry={nodes.Mesh_0003.geometry} material={materials.material_0} position={[-133.79, -5.46, 39.69]} />
        <mesh geometry={nodes.Mesh_1003.geometry} material={materials.material_0} position={[-133.79, -5.46, 39.69]} />
      </group>
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
        height: '50vh',
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
  