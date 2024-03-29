import random


class Skill(object):
	
	def __init__(self, name, chance):
		self.__name = name
		self._chance = chance

	@property
	def name(self):
		return self.__name

	@property
	def chance(self):
		return self._chance

	@chance.setter
	def chance(self, chance):
		self._chance = chance


class Property(object):

	def __init__(self, name, minimum, maximum):
		self.__name = name
		self._min = minimum
		self._max = maximum

	@property
	def name(self):
		return self.__name

	@property
	def min(self):
		return self._min

	@min.setter
	def min(self, minimum):
		self.min = minimum

	@property
	def max(self):
		return self._max

	@max.setter
	def max(self, maximum):
		self.max = maximum


class Player(object):
	
	def __init__(self, name):
		self._name = name
		self._damage = 0		
		self._health = 0
		self._strength = 0
		self._defence = 0
		self._speed = 0
		self._luck = 0
		self.properties = []

	def initialize(self): #properties is a list of Propery objects  
		if len(self.properties) != 5:
			print "Incomplete properties"
			return
		self.health = random.randint(self.properties[0].min, self.properties[0].max+1);
		self.strength = random.randint(self.properties[1].min, self.properties[1].max+1);
		self.defence = random.randint(self.properties[2].min, self.properties[2].max+1);
		self.speed = random.randint(self.properties[3].min, self.properties[3].max+1);
		self.luck = random.randint(self.properties[4].min, self.properties[4].max+1);
		
		self.print_properties()

	def print_properties(self):
		print self.name, " properties:"
		print "health:", self.health
		print "strength", self.strength
		print "defence", self.defence
		print "speed", self.speed
		print "luck", self.luck

	def print_update(self):
		print self.name, ": New health ", self.health
		print self.name, " New luck ", self.luck
	
	@property
	def health(self):
		return self._health

	@health.setter
	def health(self, health):
		self._health = health

	@property
	def strength(self):
		return self._strength

	@strength.setter
	def strength(self, strength):
		self._strength = strength

	@property
	def defence(self):
		return self._defence

	@defence.setter
	def defence(self, defence):
		self._defence = defence
	
	@property
	def speed(self):
		return self._speed

	@speed.setter
	def speed(self, speed):
		self._speed = speed

	@property
	def luck(self):
		return self._luck

	@luck.setter
	def luck(self, luck):
		self._luck = luck

	@property
	def damage(self):
		return self._damage

	@damage.setter
	def damage(self, damage):
		self._damage = damage

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	def get_luck(self):
		self._luck = random.randint(self.properties[4].min, self.properties[4].max);

	
class Hero(Player):
	
	def __init__(self, name):
		Player.__init__(self, name)
		self.skills = [	
					Skill("rapid_strike", 10), 
					Skill("magic_shield", 20)
			      ]
		self.properties = [
					Property("health", 70, 100), 
				   	Property("strength", 70, 80), 
					Property("defence", 45, 55), 
					Property("speed", 40, 50), 
					Property("luck", 10, 30)
				  ];
		self._strike = False
		self._shield = False

	@property
	def strike(self):
		return self._strike	

	@strike.setter
	def strike(self, strike):
		self._strike = strike

	@property
	def shield(self):
		return self._shield

	@shield.setter
	def shield(self, shield):
		self._shield = shield

	
	def has_strike(self):
		chance = random.randint(0, 101)
		if chance <= self.skills[0].chance:
			self._strike = True
		else:
			 self._strike = False
		return self._strike

	def has_shield(self):
		chance = random.randint(0, 101)
		if chance <= self.skills[1].chance:
			self._shield = True
		else:
			 self._shield = False
		self._strike		


class Beast(Player):
	
	def __init__(self, name):
		Player.__init__(self, name)
		self.properties = [
					Property("health", 60, 90), 
					Property("strength", 60, 90), 
					Property("defence", 40, 60), 
					Property("speed", 40, 60), 
					Property("luck", 25, 40)
				  ];


class Battle(object):
	def __init__(self):
		self.rounds = 0
		self.winner = False
		self.turn = -1
		self.attacker = None
		self.defender = None
		self.hero = Hero("Orderus")
		self.beast = Beast("Beast")

	def get_players_luck(self):
		self.hero.get_luck()
		self.beast.get_luck()

	def fight(self):
		damage = self.attacker.strength - self.defender.defence
		if self.defender == self.hero and self.hero.has_shield():
			damage = damage / 2	
			self.hero.shield = False
			print "Orderus used his shield"
			
		self.defender.damage = damage
		self.defender.health -= damage

		print "Damage: ", damage
		
	def whos_turn(self):
		if self.rounds == 0:
			if self.hero.speed > self.beast.speed:
				self.turn = 0
			elif self.hero.speed == self.beast.speed:
				if self.hero.luck > self.beast.luck:
					self.turn = 0
				elif self.hero.luck == self.beast.luck:
					#find a rule
					self.turn = random.getrandbits(1)
				else:
					self.turn = 1
			else:
				self.turn = 1
		# not sure what gets lucky means
		#elif self.turn == 0 and self.hero.luck > self.beast.luck:
		#	self.turn = 0
		#elif self.turn == 1 and self.beast.luck > self.hero.luck:
		#	self.turn = 1	
		elif self.turn == 0:		
			self.turn = 1
		else:
			self.turn = 0
				

	def attack(self):
		if self.attacker == self.hero and self.hero.has_strike():
			self.defender.damage = self.attacker.strength - self.defender.defence
			self.defender.health -= self.defender.damage
			self.hero.strike = False
			print ("Hero used his strike")
			self.rounds -= 1
		else:
			self.whos_turn()
			if self.turn == 0:
				self.attacker = self.hero
				self.defender = self.beast
			else:
				self.attacker = self.beast
				self.defender = self.hero
			
			print "Attacker:", self.attacker.name
			print "Defender:", self.defender.name	
				
			self.fight()
						 

	def play(self):
		self.hero.initialize()
		self.beast.initialize()

		while (self.rounds < 20) or not self.winner:
			self.get_players_luck()
			self.attack()
			self.rounds += 1
			self.hero.print_update()
			self.beast.print_update()
			if self.hero.health <= 0 or self.beast.health <= 0:
				self.winner = True
				break

		if self.winner:
			if self.hero.health <= 0:
				print "Beasts won"
			else:
				print "Hero won"
		else:
			print "No one won, both are still alive"


if __name__ == "__main__":
    
	battle = Battle()
	battle.play()
		
		

