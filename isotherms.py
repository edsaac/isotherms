import streamlit as st
import numpy as np

def main():
    st.set_page_config(
        page_title="Isotherms", 
        page_icon="🌪️", 
        layout="centered", 
        initial_sidebar_state="auto", 
        menu_items=None)
    
    with open("assets/style.css") as f:
        st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)
    
    r"""
    # Isotherms

    $$
        \textsf{Sorption isotherm:} \quad Q = f(C)
    $$
    
    |Parameter|Description|Units|
    |:----:|:-----------|:----|
    |$Q$  |Concentration of compound retained on the solid phase | $\dfrac{\textrm{kg}_\textsf{solute}}{\textrm{kg}_\textsf{adsorbent}}$ |
    |$C$  |Solute concentration remaining in the mobile phase    | $\dfrac{\textrm{kg}_\textsf{solute}}{\textrm{L}_\textsf{solution}}$ |

    
    &nbsp;
    """
    
    st.caption("Source: [Limousin et al., 2007](https://doi.org/10.1016/j.apgeochem.2006.09.010)")
    st.image("https://ars.els-cdn.com/content/image/1-s2.0-S0883292706002629-gr6.jpg")
    r"""
    
    *See Table 1 from [Limousin et al., 2007](https://doi.org/10.1016/j.apgeochem.2006.09.010)*
    
    ********
    ## Linear model

    $$
        Q = kC
    $$

    |Parameter|Description|Units|
    |:----:|:-----------|:----:|
    |$k$  |Fitting parameter | $\dfrac{\textrm{L}_\textsf{solution}}{\textrm{kg}_\textsf{adsorbent}}$ |

    """

    with st.echo():
        def linear(C:float, k:float)->float:
            return k * C
    
    r"""
    ********
    ## Freundlich model

    $$
        Q = kC^n
    $$

    |Parameter|Description|Units|
    |:----:|:-----------|:----:|
    |$k$  |Fitting parameter | $\left(\dfrac{\textrm{L}_\textsf{solution}}{\textrm{kg}_\textsf{adsorbent}}\right)^n$ |
    |$n$  |Fitting parameter | - |

    """

    with st.echo():
        def freundlich(C:float, k:float, n:float)->float:
            return k * np.power(C, n)
        
    r"""
    ********
    ## Temkin model

    $$
        Q = k_1 \ln{C} + k_2
    $$

    |Parameter|Description|Units|
    |:----:|:-----------|:----:|
    |$k_1$  |Fitting parameter | ? |
    |$k_2$  |Fitting parameter | ? |

    """

    with st.echo():
        def temkin(C:float, k1:float, k2:float)->float:
            return k1 * np.log(C) + k2
    
    r"""
    ********
    ## Langmuir model

    $$
        Q = Q_{\textsf{max}} \, \dfrac{kC}{1 + kC}
    $$

    |Parameter|Description|Units|
    |:----:|:-----------|:----:|
    |$Q_\textsf{max}$  |Fitting parameter | ? |
    |$k$  |Fitting parameter | ? |

    """

    with st.echo():
        def langmuir(C:float, Qmax:float, k:float)->float:
            return Qmax * (k*C)/(1 + k*C)
        
    r"""
    ********
    ## Langmuir-Freundlich model

    $$
        Q = Q_{\textsf{max}} \, \dfrac{kC^n}{1 + \left(kC\right)^n}
    $$

    |Parameter|Description|Units|
    |:----:|:-----------|:----:|
    |$Q_\textsf{max}$  |Fitting parameter | ? |
    |$k$  |Fitting parameter | ? |
    |$n$  |Fitting parameter | ? |


    """

    with st.echo():
        def langmuir_freundlich(C:float, Qmax:float, k:float, n:float)->float:
            return Qmax * (k * np.power(C,n))/(1 + np.power(k*C,n))

    r"""
    ********
    ## Generalized Langmuir model

    $$
        Q = Q_{\textsf{max}} \, \left(\dfrac{kC}{1 + kC}\right)^n
    $$

    |Parameter|Description|Units|
    |:----:|:-----------|:----:|
    |$Q_\textsf{max}$  |Fitting parameter | ? |
    |$k$  |Fitting parameter | ? |
    |$n$  |Fitting parameter | ? |


    """

    with st.echo():
        def general_langmuir(C:float, Qmax:float, k:float, n:float)->float:
            return Qmax * np.power((k*C)/(1 + k*C), n)

    r"""
    ********
    ## Redlich-Peterson model

    $$
        Q = Q_{\textsf{max}} \, \dfrac{kC}{1 + \left(kC\right)^n}
    $$

    |Parameter|Description|Units|
    |:----:|:-----------|:----:|
    |$Q_\textsf{max}$  |Fitting parameter | ? |
    |$k$  |Fitting parameter | ? |
    |$n$  |Fitting parameter | ? |


    """

    with st.echo():
        def redlich_peterson(C:float, Qmax:float, k:float, n:float)->float:
            return Qmax * (k*C)/(1 + np.power(k*C,n))
        
    
if __name__ == "__main__":
    main()