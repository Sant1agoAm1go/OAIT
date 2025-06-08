import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Настройка стиля
plt.style.use('seaborn-v0_8-whitegrid')

# Создание фигуры
fig, ax = plt.subplots(figsize=(16, 10), subplot_kw={'polar': True})
plt.subplots_adjust(right=0.65, left=0.05, top=0.9, bottom=0.1)

# Конфигурация радара
RINGS = ['ADOPT', 'TRIAL', 'ASSESS', 'HOLD']
RADII = [2.0, 3.5, 5.0, 6.5]
QUADRANTS = ['Технологии', 'Языки и фреймворки', 'Инструменты', 'Платформы']
COLORS = plt.cm.tab10.colors[:4]

# Очистка элементов
ax.set_xticks([])
ax.set_yticks([])
ax.spines[:].set_visible(False)
ax.grid(False)

# 1. Рисуем кольца с названиями
for radius, label in zip(RADII, RINGS):
    ax.plot(np.linspace(0, 2 * np.pi, 100), [radius] * 100,
            color='gray', linestyle='--', linewidth=0.7, alpha=0.5)

    ax.text(np.pi / 2, radius - 0.7, label,
            ha='center', va='center',
            fontsize=11, color='darkblue',
            bbox=dict(facecolor='white', alpha=0.9, boxstyle='round,pad=0.2'))

# 2. Устанавливаем границы
ax.set_ylim(0, RADII[-1])

# 3. Квадранты с горизонтальными названиями
angles = np.linspace(0, 2 * np.pi, 4, endpoint=False)
for angle, quadrant, color in zip(angles, QUADRANTS, COLORS):
    # Заливка квадрантов
    ax.fill_between(np.linspace(angle, angle + np.pi / 2, 50),
                    0, RADII[-1],
                    color=color, alpha=0.15)

    # Названия квадрантов горизонтально
    ax.text(angle + np.pi / 4, RADII[-1] + 1.2, quadrant,
            ha='center', va='center',
            fontsize=12, rotation=0,
            bbox=dict(facecolor='white', alpha=0.9, edgecolor='none'))

# 4. Данные технологий (полная версия)
technologies = {
    'Технологии': {
        'ADOPT': ['Socket.io', 'REST API', 'PostgreSQL'],  # Заменен Firebase DB
        'TRIAL': ['Cloudinary'],
        'ASSESS': ['WebRTC', 'RTMP Server'],
        'HOLD': ['MQTT/gRPC']
    },
    'Языки и фреймворки': {
        'ADOPT': ['Python/Flask', 'Node.js/Express', 'React'],  # Добавлен Python
        'TRIAL': ['Next.js'],
        'ASSESS': ['SvelteKit', 'NestJS'],
        'HOLD': ['Go/Ruby']
    },
    'Инструменты': {
        'ADOPT': ['Git/GitHub', 'Docker'],
        'TRIAL': ['VSCode Live Share'],
        'ASSESS': ['Terraform', 'Prometheus'],
        'HOLD': ['Kubernetes']
    },
    'Платформы': {
        'ADOPT': ['Vercel/Heroku', 'Firebase'],
        'TRIAL': ['DigitalOcean'],
        'ASSESS': ['AWS Lightsail', 'Supabase'],
        'HOLD': ['On-Prem']
    }
}

# 5. Легенда (полная версия)
legend_elements = []
for quad_color, quadrant in zip(COLORS, QUADRANTS):
    # Заголовок квадранта
    legend_elements.append(Patch(
        facecolor=quad_color,
        edgecolor='black',
        label=f' {quadrant}'
    ))

    # Элементы по кольцам
    for ring in RINGS:
        items = technologies[quadrant][ring]
        legend_elements.append(Patch(
            facecolor='white',
            edgecolor=quad_color,
            label=f"   {ring}: " + ', '.join(items)
        ))

# Размещаем легенду
legend = ax.legend(
    handles=legend_elements,
    loc='center left',
    bbox_to_anchor=(1.02, 0.5),
    fontsize=10,
    title="Детализация Tech Radar",
    frameon=True,
    borderpad=1.5,
    handlelength=1.8,
    handleheight=2.4
)

plt.title("Tech Radar\n", fontsize=18, pad=35, fontweight='bold')
plt.show()
