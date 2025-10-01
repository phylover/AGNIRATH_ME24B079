def calculate_steady_state_temp(T_a, tau):
    T_w = 323  # Initial guess
    while True:
        # 1. Magnet temperature
        T_m = (T_a + T_w) / 2
        
        # 2. Remanence
        B = 1.32 - 1.2e-3 * (T_m - 293)
        
        # 3. Phase current
        i = 0.561 * B * tau
        
        # 4. Resistance
        R = 0.0575 * (1 + 0.0039 * (T_w - 293))
        
        # 5. Copper loss
        P_c = 3 * (i**2) * R
        
        # 6. Eddy loss
        P_e = (9.602e-6 * (B * tau)**2) / R
        
        # 7. Update winding temperature
        new_T_w = 0.455 * (P_c + P_e) + T_a
        
        # Check convergence
        if abs(new_T_w - T_w) < 1:
            return round(new_T_w, 1)
        
        # Update for next iteration
        T_w = new_T_w
