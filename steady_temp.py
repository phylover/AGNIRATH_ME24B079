def calculate_steady_state_temp(T_a, tau):
    T_w = 323  # Initial guess
    while True:
        # Temperature of the magnet 
        T_m = (T_a + T_w) / 2
        
        B = 1.32 - 1.2e-3 * (T_m - 293)
        
        # Phase current equation
        i = 0.561 * B * tau
        
        # Resistance at temp T_w
        R = 0.0575 * (1 + 0.0039 * (T_w - 293))
        
        # Copper losses
        P_c = 3 * (i**2) * R
        
        # Eddy losses
        P_e = (9.602e-6 * (B * tau)**2) / R
        
        # winding temp after this iteration 
        a = 0.455 * (P_c + P_e) + T_a
        
        # Break from the loop if difference is less than 1k
        if abs(a- T_w) < 1:
            return round(a, 1)
        
        # Update for next iteration
        T_w =a
