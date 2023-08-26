import tkinter as tk
import numpy as np
from sqlite3 import *


class Skin:
    
    """This class helps you to calculate all sorts of skin phenomenon and analize it.
    Hereafter skin refers back to any reason reduces the oil well production and causes pressure drop
    in that well."""
    
    """
        Rw (inches):    Well radius
    """
    
    def __init__(self, Rw):
    
        self.Rw = float(Rw)
    
    def perforation(self, lp, theta, spf, Rd, Rc, Rp, anisotropy, damage_ratio, crushed_ratio):
        
        """This function helps you to find skin due to the perforation job.
            We know that the total perforation skin is the sum of vertical, horizontal,
            wellbore and crushed zone skin. In other word:
            Sp = Swb + Sc + Sh + Sv
            
            lp (inches):    perforation Length
            theta:  Phasing angle in degree
            SPF: shut density
            Kv/Kh:  anisotropy
            Kd/K:   damage permeability to res. permeability
            Kc/k:  crushed permeability to res. permeability
            Rd (inches):  damage zone radius
            Rc (inches):  crushed zone radius
            Rp (inches):  Perforation tunnel radius
            h (inches): spaced between perforations
        """
        lp = float(lp)
        theta = int(theta); spf = int(spf); Rd = float(Rd); Rc = float(Rc); Rp = float(Rp); anisotropy = float(anisotropy); damage_ratio = float(damage_ratio); crushed_ratio = float(crushed_ratio)
        
        ld = Rd - self.Rw
        h = 12 / spf
        RpD = (Rp / (2*h)) * (1 + (anisotropy ** 0.5))
        hD = (h / lp) * ((1 / anisotropy) ** 0.5)
        RwD = (self.Rw / (self.Rw + lp))
        
        #connecting to our database
        conn = connect('tables.db')
        c = conn.cursor()
        
        a1 = c.execute(f"""SELECT a1 FROM perforation_vertical where phasing == {theta} LIMIT 500""").fetchone()[0]
        a2 = c.execute(f"""SELECT a2 FROM perforation_vertical where phasing == {theta} LIMIT 500""").fetchone()[0]
        b1 = c.execute(f"""SELECT b1 FROM perforation_vertical where phasing == {theta} LIMIT 500""").fetchone()[0]
        b2 = c.execute(f"""SELECT b2 FROM perforation_vertical where phasing == {theta} LIMIT 500""").fetchone()[0]
        C1 = c.execute(f"""SELECT C1 FROM perforation_wellbore where phasing == {theta} LIMIT 500""").fetchone()[0]
        C2 = c.execute(f"""SELECT C2 FROM perforation_wellbore where phasing == {theta} LIMIT 500""").fetchone()[0]
        a = a1 * np.log10(RpD) + a2
        b = b1 * RpD + b2
        
        if ld > lp:
            if theta == 0:
                
                Sh = np.log((4*self.Rw) / lp)
                
            
            else:
                
                Sh = np.log((self.Rw) / (c.execute(f"""SELECT alpha FROM [perforation_horizontal] WHERE phasing == {theta} LIMIT 500""") * (self.Rw + lp)))
                
            Sv = (10 ** a) * (hD ** (b - 1)) * (RpD ** b)
            Swb = C1 * np.exp(C2 * RwD)
            Sc = (h / lp) * ((1 / crushed_ratio) - 1) * np.log(Rc / Rp)
            Sp = Sv + Swb + Sc + Sh
            Sp = ((1 / damage_ratio) - 1) * np.log(Rd/self.Rw) + (1 / damage_ratio) * Sp
            
        elif ld < lp:
            
            lp_prime = lp - (1 - damage_ratio) * ld
            Rw_prime = self.Rw + (1 - damage_ratio) * ld 
            hD_prime = (h / lp_prime) * ((1 / anisotropy) ** 0.5)
            RwD_prime = (Rw_prime) / (Rw_prime + lp_prime)
            
            if theta == 0:
                
                Sh = np.log((4*self.Rw) / lp_prime)
                            
            else:
                
                Sh = np.log((self.Rw) / (c.execute(f"""SELECT alpha FROM [perforation_horizontal] WHERE phasing == {theta} LIMIT 500""").fetchone()[0] * (Rw_prime + lp_prime)))
            
            Sv = (10 ** a) * (hD_prime ** (b - 1)) * (RpD ** b)
            Swb = C1 * np.exp(C2 * RwD_prime)
            Sc = (h / lp_prime) * ((1 / crushed_ratio) - 1) * np.log(Rc / Rp)
            Sp = Sv + Swb + Sc + Sh
        
        conn.commit()
        conn.close()
        
        return Sp