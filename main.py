from multivariable_chainRule import MultiVariableChainRule

if __name__== "__main__":
    MultiVariableChainRule()
    while True:
        menu=input("Continue? Y/N\n")
        if menu=="y" or menu=="Y":
            MultiVariableChainRule()
        elif menu=="n" or menu=="N":
            raise SystemExit()