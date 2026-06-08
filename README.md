# ChromaPlex OS Compiler Toolchain

Velkommen til maskinrummet for fremtidens optiske datalagring. Dette repository indeholder en eksekverbar software-stack for ChromaPlex OS – et eksperimentelt sprog og værktøjssæt designet til at modellere 5D optisk datalagring i glaskrystaller (*fused silica*).

Her finder du den virtuelle maskine (VM), CPA-assembleren (ChromaPlex Assembly) og CPL-compileren. Det er her, idéerne om rumlig voxel-adressering, bølgelængdekanaler, optisk multipleksing og eksponentiel talrepræsentation bliver omsat til testbar simulator- og VM-kode.

🔗 **[Hovedprojekt: Se selve ChromaPlex programmeringssproget og kildekoden her](https://github.com/Janus5G/chromaplex-os)**

👉 **[Forstå fysikken og arkitekturen: Læs den fulde ChromaPlex v2.0 specifikation her](https://github.com/Janus5G/ChromaPlex-v2.0-Specification-Architecture-Documentation)**

🎮 **[Prøv 3D Simulatoren direkte i browseren her](https://Janus5G.github.io/chromaplex-os-compiler/)**

## ℹ️ **[Er du fra pressen? Læs vores FAQ her for hurtige svar.](FAQ.md)**

---

## Installation og test

For at trække projektet ned og køre det lokalt:

```bash
git clone https://github.com/Janus5G/chromaplex-os-compiler.git
cd chromaplex-os-compiler
pip install -e .
```

# ChromaPlex OS

ChromaPlex OS er et domænespecifikt sprog (DSL) designet til at styre laser-baseret læsning/skrivning i 3D-krystaller (fused silica).

## Funktioner

- **5 laserbølgelængder**: 350nm (UV), 405nm (Violet), 473nm (Blå), 532nm (Grøn), 650nm (Rød)
- **Eksponentiel datakomprimering**: Tal gemmes som 2^e + rest
- **3D voxel-adressering**: Præcis (x,y,z) positionering i krystallen
- **To sprog**: CPA (Assembly) og CPL (Højniveau)

## BEMÆRKNING TIL VERSION 
For at få en ikke ændret eller fejlrettet version forbliver .json og unpakc_chromaplex.py det samme vil du ha en fejlrettet version
der virker med det nyeste udviklerværktøjer jeg laver så download .zip i stedet. 

## Installation

Kræver Python 3.9+.

```bash
pip install -e .
```

## Brug

```bash
chromaplex compile program.cpl -o program.bin
chromaplex run program.bin
chromaplex run program.cpl --source
```

## Projektstruktur

```text
chromaplex_os/
    __init__.py             - Pakkeinitiering
    spec.py                 - Specifikationer og konstanter
    assembler.py            - CPA assembler
    compiler.py             - CPL compiler
    vm.py                   - Virtual Machine
    storage.py              - Krystalsimulering
    hardware.py             - Laserhardware-simulering
    cli.py                  - Kommandolinjeinterface
    visual_demo.py          - Visualiseringsværktøj
    visualization_viewer.py - Visualisering af krystaldata
examples/
    hello.cpl               - Simpelt CPL program
    fibonacci.cpl           - Fibonacci demonstration
    generate_visualization.cpl - Visualiseringsdatagenerator
tests/
    test_assembler.py       - Assembler tests
setup.py                    - Installationsscript
```
## Relaterede repositories

- [Cplex editor til ChromaPlex/CPL](https://github.com/Janus5G/Cplex)
