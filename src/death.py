
class Death:
    """Luokka, joka tarkistaa osuuko pelaaja seinään.
    """
    @classmethod
    def check_death(cls,posx,posy):
        """_summary_

        Args:
            posx: Pelaajan x koordinaatti.
            posy: Pelaajan y koordinaatti.

        Returns:
            True jos pelaaja osuu seinään, muuten False.
        """
        if posx >= 560 or posy >= 560 or posx < 40 or posy < 40:
            return True
        return False
