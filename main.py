def calcu_tri(funt: str):
    function_type = funt[:3]
    function_x = raw = float(funt[3:])
    msg = f'### 计算过程\n\n**输入：**\n${function_type}({function_x}°)$\n'

    negative1 = False

    count_360 = 0
    count_180 = 0
    count_90 = 0
    if function_x < 0: # 诱导公式3
        if function_type in ['sin', 'tan']:
            function_x = -function_x
            negative1 = True
            msg += f'\n$$\n= -{function_type}({function_x}°)$$'
        elif function_type in ['cos']:
            function_x = -function_x
            negative1 = False
            msg += f'\n$$\n= {function_type}({function_x}°)$$'
    
    if function_x >= 360: # 诱导公式1
        count_360 = int(function_x // 360)
        function_x -= count_360*360
        raw1 = function_x
        msg += '\n$$\n\\begin{aligned}'
        msg += f'&={"-" if negative1 else ""}{function_type}({raw1}° + {count_360} \\times 360°) \\\\'
        msg += f'&={"-" if negative1 else ""}{function_type}({raw1}°) \end{{aligned}}$$'

    if function_x >= 180:# 诱导公式 2
        if function_type in ['sin', 'cos']: 
            count_180 = int(function_x // 180)
            function_x -= count_180*180
            raw2 = function_x
            msg += '\n$$\n\\begin{aligned}'
            msg += f'&={"-" if negative1 else ""}{function_type}({raw2}° + {count_180} \\times 180°) \\\\'

            negative1 = False if negative1 else True 

            msg += f'&={"-" if negative1 else ""}{function_type}({raw2}°) \end{{aligned}}$$'
        if function_type in ['tan']:
            count_180 = int(function_x // 180)
            function_x -= count_180*180
            raw2 = function_x
            msg += '\n$$\n\\begin{aligned}'
            msg += f'&={"-" if negative1 else ""}{function_type}({raw2}° + {count_180} \\times 180°) \\\\'

            negative1 = True if negative1 else False

            msg += f'&={"-" if negative1 else ""}{function_type}({raw2}°) \end{{aligned}}$$'

    if function_x >= 90: # 诱导公式 4
        if function_type in ['cos', 'tan']:
            raw3 = function_x
            function_x = 180 - function_x
            msg += '\n$$\n\\begin{aligned}'
            msg += f'&={"-" if negative1 else ""}{function_type}(180° - {raw3}°) \\\\'

            negative1 = False if negative1 else True 

            msg += f'&={"-" if negative1 else ""}{function_type}({function_x}°) \end{{aligned}}$$'

        if function_type in ['sin']:
            raw3 = function_x
            function_x = 180 - function_x
            msg += '\n$$\n\\begin{aligned}'
            msg += f'&={"-" if negative1 else ""}{function_type}(180° - {raw3}°) \\\\'

            negative1 = True if negative1 else False 

            msg += f'&={"-" if negative1 else ""}{function_type}({function_x}°) \end{{aligned}}$$'

    if function_type in ['sin', 'cos']:# 公式5
        count_90 = function_x
        raw4 = 90 - function_x
        msg += '$$\n\\begin{aligned}'
        msg += f'&={"-" if negative1 else ""}{function_type}(90° - {count_90}°) \\\\'
        msg += f'&={"-" if negative1 else ""}{"sin" if function_type == "cos" else "cos"}({raw4}°) \end{{aligned}}$$'

    msg += '\n\n---\n'

    return msg
