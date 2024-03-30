# Generating Kernels for Jupyter using Python Virtual Environments.
So I saw [this](https://www.linkedin.com/pulse/how-use-virtual-environment-inside-jupyter-lab-sina-khoshgoftar)
post on linkedin while trying to figure out how install third-party modules in Jupyter Lab and while
helpful, it's a bit of an eyesore.

Instead of complaining about it though I just decided to never have to look at it again by
immortalizing the basic principle in a third-party module that generates Jupyter kernels for me.

The command itself isn't particularly confusing; simply install `ipykernel` to the environment and
export as a kernel locally available to any lab instance you may be running.

```
python3 -m venv $NEW_ENVIRONMENT;
source $NEW_ENVIRONMENT/bin/activate;
pip install ipykernel;
python3 -m ipykernel install --user --name=$NEW_ENVIRONMENT;
```

## The Code
The package can be invoked from the command line, and accepts a single mandatory argument which can either be a filepath or a valid directory name.

If the latter is given, then it will create the kernel in the current working directory; A filepath will create it at the given location and assume the deepest directory along the path to be the name of the module.

Also included is a bash-only version that requires a filepath and a name.  At this point in the process, neither executable allows for the specification of other modules to install while installing `ipykernel`; but the next version will.