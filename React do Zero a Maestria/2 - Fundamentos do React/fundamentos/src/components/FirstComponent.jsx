// arquivo de estilo

import MyComponents from "./MyComponents";

const FirstComponent = () => {

    // Essa função realiza...
    /*
    Multiplas linhas
    */
    return(
        <div>
            {/* Algum comentário. */}
            <h1> My first component</h1>
            <p className="teste">Meu texto</p>
            <MyComponents/>
            
        </div>
    );
};

export default FirstComponent;