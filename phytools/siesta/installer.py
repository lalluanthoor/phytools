"""Install Siesta and dependencies."""
import click

from phytools.base.installer import BaseInstaller


class SiestaInstaller(BaseInstaller):
    """Installs Siesta suite."""
    REQUIRED_OS_PACKAGES = ["python", "curl", "unzip", "hwloc", "sysstat", "build-essential",
                            "g++", "gfortran", "libreadline-dev", "m4", "xsltproc", "mpich",
                            "libmpich-dev"]

    def __init__(self, config):
        super().__init__(config)

    def pre_installation(self):
        pass

    def installation(self):
        pass

    def post_installation(self):
        click.echo("Installation of Siesta suite completed.", file=self.config.log_file)
        click.echo("Siesta binaries siesta, transiesta and tbtrans installed to /usr/local/bin.",
                   file=self.config.log_file)